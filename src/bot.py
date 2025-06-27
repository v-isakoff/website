"""Minimal Telegram bot using aiogram 3.x"""
import asyncio
import logging
import os
try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional dependency
    def load_dotenv(*args, **kwargs):
        return False

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import CommandStart
from aiogram.types import Message
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:  # pragma: no cover - fallback for environments without python-dotenv
    def load_dotenv() -> None:
        return None

logging.basicConfig(level=logging.INFO)
load_dotenv()

load_dotenv()

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
    try:
        await dp.start_polling(bot)
    except TelegramAPIError as e:
        logging.exception("Telegram API error: %s", e)

if __name__ == "__main__":
    asyncio.run(main())
