import os
import importlib
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

# Ensure environment variable is set before importing the bot
os.environ.setdefault("BOT_TOKEN", "test-token")

bot = importlib.import_module("src.bot")

@pytest.mark.asyncio
async def test_start_handler_sends_greeting():
    message = SimpleNamespace(answer=AsyncMock())
    await bot.start(message)
    message.answer.assert_awaited_with("Hello, I'm alive!")
