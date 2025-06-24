from aiogram import types, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.enums import ChatAction

from keyboards import main_menu_kb
from messages import load_messages

async def cmd_start(message: types.Message):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    msgs = load_messages()
    await message.answer_photo(
        photo=FSInputFile("static/main.jpg"),
        caption=msgs["main_menu_text"],
        reply_markup=main_menu_kb()
    )

def register(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
    dp.callback_query.register(main_menu, F.data=="menu")

async def main_menu(call: types.CallbackQuery):
    await call.bot.send_chat_action(call.message.chat.id, ChatAction.TYPING)
    msgs = load_messages()
    await call.message.answer(msgs["main_menu_text"], reply_markup=main_menu_kb())
    await call.answer()
