from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from messages import load_messages

def main_menu_kb():
    msgs = load_messages()
    builder = InlineKeyboardBuilder()
    builder.button(text=msgs["button_stats"], callback_data="stats")
    builder.button(text=msgs["button_settings"], callback_data="settings")
    builder.button(text=msgs["button_exercise"], callback_data="exercise")
    builder.adjust(2)
    return builder.as_markup()

def settings_kb():
    msgs = load_messages()
    builder = InlineKeyboardBuilder()
    builder.button(text=msgs["button_change_reminder"], callback_data="change_reminder")
    return builder.as_markup()
