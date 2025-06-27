from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    """Handle /start command."""
    await message.answer("Hello, I'm alive!")
