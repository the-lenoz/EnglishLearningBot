import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers.menu_handler import register as menu_register
from handlers.settings_handler import register as settings_register
from handlers.stats_handler import register as stats_register
from handlers.exercise_handler import register as exercise_register
from services.scheduler import start as scheduler_start
from database.db import engine
from database.models import Base

async def on_startup(dp: Dispatcher):
    # create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    scheduler_start()

def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    menu_register(dp)
    settings_register(dp)
    stats_register(dp)
    exercise_register(dp)
    executor.start_polling(dp, on_startup=on_startup)

if __name__ == "__main__":
    main()
