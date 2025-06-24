from aiogram import types, F, Dispatcher
from messages import load_messages
from services.ai_api import generate_image, translate_text, check_translation
from database.db import get_db
from database.models import Word, UserWord, User

async def start_exercise(call: types.CallbackQuery):
    msgs = load_messages()
    await call.message.answer(msgs["prompt_word"])
    await call.answer()

async def handle_word(message: types.Message):
    session_gen = get_db()
    async for session in session_gen:
        # lookup or create word, check stage...
        pass

def register(dp: Dispatcher):
    dp.callback_query.register(start_exercise, F.data=="exercise")
    dp.message.register(handle_word)
