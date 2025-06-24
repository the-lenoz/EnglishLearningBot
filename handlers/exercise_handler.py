from aiogram import types, F, Dispatcher
from messages import load_messages
from services.ai_api import generate_image, translate_text, check_translation
from database.db import get_db
from database.models import Word, UserWord, User
from sqlalchemy import select

async def start_exercise(call: types.CallbackQuery):
    msgs = load_messages()
    await call.message.answer(msgs["prompt_word"])
    await call.answer()

async def handle_word(message: types.Message):
    msgs = load_messages()
    async for session in get_db():
        # Ensure user exists
        result = await session.execute(select(User).where(User.telegram_id == message.from_user.id))
        user = result.scalars().first()
        if not user:
            user = User(telegram_id=message.from_user.id)
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
            await message.answer_photo(photo=img, caption=msgs["flashcard"].format(word=text, translation=translation))
        else:
            # Word already learned: ask for translation
            await message.answer(msgs["ask_translation"].format(word=text))
        return

def register(dp: Dispatcher):
    dp.callback_query.register(start_exercise, F.data=="exercise")
    dp.message.register(handle_word)
