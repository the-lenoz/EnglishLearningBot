from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from messages import load_messages

def main_menu_kb():
    msgs = load_messages()
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton(msgs["button_stats"], callback_data="stats"),
        InlineKeyboardButton(msgs["button_settings"], callback_data="settings"),
        InlineKeyboardButton(msgs["button_exercise"], callback_data="exercise")
    )
    return kb

def settings_kb():
    msgs = load_messages()
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(msgs["button_change_reminder"], callback_data="change_reminder")
    )
    return kb
