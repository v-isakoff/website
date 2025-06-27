"""Minimal Telegram bot using aiogram 3.x"""

import asyncio
import logging
import os
from contextlib import suppress

from aiogram import Bot, Dispatcher

from .handlers import register_handlers

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")


def setup_logging() -> None:
    """Configure root logger."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


async def on_startup(bot: Bot) -> None:
    logging.getLogger(__name__).info("Starting bot")


async def on_shutdown(bot: Bot) -> None:
    logging.getLogger(__name__).info("Shutting down bot")


async def main() -> None:
    """Run the bot."""
    setup_logging()
    dp = Dispatcher()
    register_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    bot = Bot(TOKEN)
    try:
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        pass
    finally:
        await bot.session.close()


if __name__ == "__main__":
    with suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())
