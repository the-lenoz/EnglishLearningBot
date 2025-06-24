from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import REMINDER_TIME
import asyncio
from database.db import AsyncSessionLocal
from sqlalchemy import select
from database.models import User, UserWord, Word
from messages import load_messages
from handlers.exercise_handler import user_pending

scheduler = AsyncIOScheduler()

async def send_scheduled_exercise(bot, user_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.telegram_id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            return
        result = await session.execute(select(UserWord).where(UserWord.user_id == user.id))
        uw = result.scalars().first()
        if not uw:
            return
        result = await session.execute(select(Word).where(Word.id == uw.word_id))
        word = result.scalar_one()
        word_text = word.en
    msgs = load_messages()
    user_pending[user_id] = word_text
    await bot.send_message(user_id, msgs["ask_translation"].format(word=word_text))

def schedule_reminder(bot, user_id: int):
    hour, minute = map(int, REMINDER_TIME.split(":"))
    scheduler.add_job(
        lambda: asyncio.create_task(send_scheduled_exercise(bot, user_id)),
        'cron', hour=hour, minute=minute, id=f"reminder_{user_id}"
    )

def start():
    scheduler.start()
