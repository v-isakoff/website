import importlib
import sys
import types
import asyncio
import pytest


def make_aiogram(bot_init=None, start_polling=None):
    """Create a minimal aiogram mock."""
    class Bot:
        def __init__(self, token: str):
            if bot_init:
                bot_init(token)

    class Dispatcher:
        def __init__(self):
            pass

        def message(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator

        async def start_polling(self, bot):
            if start_polling:
                await start_polling(bot)

    aiogram = types.ModuleType("aiogram")
    aiogram.Bot = Bot
    aiogram.Dispatcher = Dispatcher

    filters = types.ModuleType("aiogram.filters")
    filters.CommandStart = object
    aiogram.filters = filters

    types_mod = types.ModuleType("aiogram.types")
    types_mod.Message = object
    aiogram.types = types_mod

    sys.modules["aiogram"] = aiogram
    sys.modules["aiogram.filters"] = filters
    sys.modules["aiogram.types"] = types_mod


async def call_main(monkeypatch, bot_init=None, start_polling=None):
    make_aiogram(bot_init=bot_init, start_polling=start_polling)
    monkeypatch.setenv("BOT_TOKEN", "x")
    if "src.bot" in sys.modules:
        del sys.modules["src.bot"]
    bot_mod = importlib.import_module("src.bot")
    await bot_mod.main()


def test_main_runs(monkeypatch):
    calls = []

    async def sp(bot):
        calls.append(bot)

    asyncio.run(call_main(monkeypatch, start_polling=sp))
    assert len(calls) == 1


def test_bot_init_error(monkeypatch):
    async def sp(bot):
        pass

    def failing_init(token):
        raise ValueError("boom")

    with pytest.raises(RuntimeError, match="Failed to initialize Bot"):
        asyncio.run(call_main(monkeypatch, bot_init=failing_init, start_polling=sp))


def test_polling_error(monkeypatch):
    async def sp(bot):
        raise RuntimeError("oops")

    with pytest.raises(RuntimeError, match="Polling stopped unexpectedly"):
        asyncio.run(call_main(monkeypatch, start_polling=sp))


def test_missing_token(monkeypatch):
    monkeypatch.delenv("BOT_TOKEN", raising=False)
    make_aiogram()
    if "src.bot" in sys.modules:
        del sys.modules["src.bot"]
    with pytest.raises(RuntimeError, match="BOT_TOKEN environment variable is not set"):
        importlib.import_module("src.bot")
