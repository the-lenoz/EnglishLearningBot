from io import BytesIO

from aiogram import types, F, Dispatcher
from aiogram.types import BufferedInputFile

from messages import load_messages
from services.ai_api import generate_image, translate_text, check_translation
from database.db import get_db
from database.models import Word, UserWord, User
from sqlalchemy import select
# track users awaiting translation
user_pending = {}

async def start_exercise(call: types.CallbackQuery):
    msgs = load_messages()
    await call.message.answer(msgs["prompt_word"])
    await call.answer()

async def handle_word(message: types.Message):
    msgs = load_messages()
    user_id = message.from_user.id

    # if awaiting translation, process it
    if user_id in user_pending:
        orig_word = user_pending.pop(user_id)
        is_correct = await check_translation(orig_word, message.text.strip())
        correct_trans = await translate_text(orig_word)
        if is_correct:
            await message.answer(msgs["correct"])
        else:
            await message.answer(msgs["incorrect"].format(translation=correct_trans))
        img = await generate_image(orig_word)
        await message.answer_photo(photo=BufferedInputFile(img, "image.jpg"), caption=msgs["flashcard"].format(word=orig_word, translation=correct_trans))
        return

    async for session in get_db():
        # Ensure user exists
        result = await session.execute(select(User).where(User.telegram_id == user_id))
        user = result.scalars().first()
        if not user:
            user = User(telegram_id=user_id)
            session.add(user)
            await session.commit()

        text = message.text.strip()
        # Ensure word exists
        result = await session.execute(select(Word).where(Word.text == text))
        word = result.scalars().first()
        if not word:
            translation = await translate_text(text)
            word = Word(text=text, translation=translation)
            session.add(word)
            await session.commit()
        else:
            translation = word.translation

        # Check if user has learned this word
        result = await session.execute(select(UserWord).where(
            UserWord.user_id == user.id, UserWord.word_id == word.id))
        user_word = result.scalars().first()

        if not user_word:
            # First time seeing this word: create learning entry and send flashcard
            img = await generate_image(text)
            session.add(UserWord(user_id=user.id, word_id=word.id))
            await session.commit()
            await message.answer_photo(photo=BufferedInputFile(img, "image.jpg"), caption=msgs["flashcard"].format(word=text, translation=translation))
        else:
            # Word already learned: ask for translation next
            user_pending[user_id] = text
            await message.answer(msgs["ask_translation"].format(word=text))
        return

def register(dp: Dispatcher):
    dp.callback_query.register(start_exercise, F.data=="exercise")
    dp.message.register(handle_word)
