from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ChatAction

class TypingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            await event.bot.send_chat_action(event.chat.id, ChatAction.TYPING)
        elif isinstance(event, CallbackQuery) and event.message:
            await event.message.bot.send_chat_action(event.message.chat.id, ChatAction.TYPING)
        return await handler(event, data)
