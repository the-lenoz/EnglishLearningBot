import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.menu_handler import register as menu_register
from handlers.settings_handler import register as settings_register
from handlers.stats_handler import register as stats_register
from handlers.exercise_handler import register as exercise_register
from services.scheduler import start as scheduler_start
from database.db import engine
from database.models import Base


async def on_startup_hook():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    scheduler_start()

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    from middlewares.typing_middleware import TypingMiddleware
    dp.update.middleware(TypingMiddleware())
    menu_register(dp)
    settings_register(dp)
    stats_register(dp)
    exercise_register(dp)
    await on_startup_hook()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
