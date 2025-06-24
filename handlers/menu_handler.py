from aiogram import types, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import FSInputFile

from keyboards import main_menu_kb
from messages import load_messages

async def cmd_start(message: types.Message):
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
    msgs = load_messages()
    await call.message.edit_caption(msgs["main_menu_text"], reply_markup=main_menu_kb())
    await call.answer()
