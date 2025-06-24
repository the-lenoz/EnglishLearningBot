import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_API_KEY = os.getenv("AI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///db.sqlite3")
REMINDER_TIME = os.getenv("REMINDER_TIME", "09:00")
