from aiogram import types
from aiogram.dispatcher import FSMContext, Dispatcher
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
    await call.message.answer("Enter new reminder time (HH:MM):")
    await call.answer()
    # further FSM handling omitted for brevity

def register(dp: Dispatcher):
    dp.register_callback_query_handler(settings_menu, lambda c: c.data == "settings")
    dp.register_callback_query_handler(change_reminder, lambda c: c.data == "change_reminder")
