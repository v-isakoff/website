import importlib
import sys
import types


def mock_aiogram():
    class Bot:
        def __init__(self, token: str):
            self.token = token

    class Dispatcher:
        def message(self, *args, **kwargs):
            def decorator(func):
                return func
            return decorator

        async def start_polling(self, bot):
            return None

    aiogram = types.ModuleType("aiogram")
    aiogram.Bot = Bot
    aiogram.Dispatcher = Dispatcher

    filters = types.ModuleType("aiogram.filters")
    filters.CommandStart = object
    aiogram.filters = filters
    sys.modules["aiogram"] = aiogram
    sys.modules["aiogram.filters"] = filters

    types_mod = types.ModuleType("aiogram.types")
    types_mod.Message = object
    aiogram.types = types_mod
    sys.modules["aiogram.types"] = types_mod


def mock_fastapi_uvicorn():
    class FastAPI:
        def mount(self, *args, **kwargs):
            pass

    class StaticFiles:
        def __init__(self, *args, **kwargs):
            pass

    fastapi = types.ModuleType("fastapi")
    fastapi.FastAPI = FastAPI

    staticfiles = types.ModuleType("fastapi.staticfiles")
    staticfiles.StaticFiles = StaticFiles
    fastapi.staticfiles = staticfiles
    sys.modules["fastapi"] = fastapi
    sys.modules["fastapi.staticfiles"] = staticfiles

    uvicorn = types.ModuleType("uvicorn")
    uvicorn.run = lambda *args, **kwargs: None
    sys.modules["uvicorn"] = uvicorn


def test_import_bot(monkeypatch):
    monkeypatch.setenv("BOT_TOKEN", "x")
    mock_aiogram()
    assert importlib.import_module("src.bot")


def test_import_serve_web():
    mock_fastapi_uvicorn()
    assert importlib.import_module("src.serve_web")
