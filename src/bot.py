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
    """Run the bot with basic error handling."""
    try:
        bot = Bot(TOKEN)
    except Exception as exc:  # pragma: no cover - defensive
        raise RuntimeError("Failed to initialize Bot") from exc

    try:
        await dp.start_polling(bot)
    except Exception as exc:
        raise RuntimeError("Polling stopped unexpectedly") from exc

if __name__ == "__main__":
    asyncio.run(main())
