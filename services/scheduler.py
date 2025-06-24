from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import REMINDER_TIME
from aiogram import types
from aiogram.types import InputMediaPhoto
import asyncio
from database.db import AsyncSessionLocal
from datetime import datetime
from messages import load_messages

scheduler = AsyncIOScheduler()

def schedule_reminder(bot, user_id: int):
    hour, minute = map(int, REMINDER_TIME.split(":"))
    scheduler.add_job(
        lambda: asyncio.create_task(bot.send_message(user_id, load_messages()["reminder_text"])),
        'cron', hour=hour, minute=minute, id=f"reminder_{user_id}"
    )

def start():
    scheduler.start()
