"""Minimal Telegram bot using aiogram 3.x"""
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")

# Configure dispatcher
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message) -> None:
    """Handle /start command."""
    await message.answer("Hello, I'm alive!")

async def main() -> None:
    """Run the bot."""
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
