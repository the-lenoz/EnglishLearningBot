from aiogram import types, F, Dispatcher
from aiogram.enums import ChatAction

from database.db import get_db
from database.models import User
from messages import load_messages


async def stats_menu(call: types.CallbackQuery):
    await call.bot.send_chat_action(call.message.chat.id, ChatAction.TYPING)
    session_gen = get_db()
    async for session in session_gen:
        user = (await session.execute(
            User.__table__.select().where(User.telegram_id == call.from_user.id)
        )).scalar_one_or_none()
        # calculate stats...
    msgs = load_messages()
    await call.message.answer(
        msgs["stats_text"].format(words=0, reps=0, exs=0, pct=0, streak=0)
    )
    await call.answer()

def register(dp: Dispatcher):
    dp.callback_query.register(stats_menu, F.data=="stats")
