from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📈 Statistics", callback_data="stats"),
        InlineKeyboardButton("⚙️ Settings", callback_data="settings"),
        InlineKeyboardButton("📝 Start Exercise", callback_data="exercise")
    )
    return kb

def settings_kb():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("Change reminder time", callback_data="change_reminder")
    )
    return kb
