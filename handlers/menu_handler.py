from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards import main_menu_kb
from messages import load_messages

async def cmd_start(message: types.Message):
    msgs = load_messages()
    await message.answer_photo(
        photo=open("static/main.jpg", "rb"),
        caption=msgs["main_menu_text"],
        reply_markup=main_menu_kb()
    )

def register(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
    dp.register_callback_query_handler(main_menu, lambda c: c.data == "menu")

async def main_menu(call: types.CallbackQuery):
    msgs = load_messages()
    await call.message.edit_caption(msgs["main_menu_text"], reply_markup=main_menu_kb())
    await call.answer()
