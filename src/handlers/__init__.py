from aiogram import Dispatcher

from . import start


def register_handlers(dp: Dispatcher) -> None:
    """Register all handlers for the bot."""
    dp.include_router(start.router)
