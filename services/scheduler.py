import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from messages import load_messages
from services import user_current_data

scheduler = AsyncIOScheduler()

async def send_scheduled_exercise(bot, user_id: int, word_text: str):
    msgs = load_messages()
    while user_current_data.user_pending.get(user_id):
        await asyncio.sleep(1)
    user_current_data.user_pending[user_id] = word_text
    await bot.send_message(user_id, msgs["ask_translation"].format(word=word_text))

def start():
    scheduler.start()
