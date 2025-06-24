from aiogram import types, Dispatcher, F
from aiogram.fsm.context import FSMContext
from keyboards import settings_kb
from messages import load_messages
from database.db import get_db
from database.models import Setting, User
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def settings_menu(call: types.CallbackQuery):
    msgs = load_messages()
    await call.message.edit_text(msgs["settings_text"], reply_markup=settings_kb())
    await call.answer()

async def change_reminder(call: types.CallbackQuery):
    msgs = load_messages()
    await call.message.answer(msgs["enter_reminder_prompt"])
    await call.answer()
    # further FSM handling omitted for brevity

def register(dp: Dispatcher):
    dp.callback_query.register(settings_menu, F.data=="settings")
    dp.callback_query.register(change_reminder, F.data=="change_reminder")
