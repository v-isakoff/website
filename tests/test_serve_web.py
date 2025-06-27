import importlib
import sys
import types


def make_fastapi():
    mounted = []

    class FastAPI:
        def __init__(self):
            pass

        def mount(self, path, app, name=None):
            mounted.append((path, app.directory, app.html, name))

    class StaticFiles:
        def __init__(self, directory, html=False):
            self.directory = directory
            self.html = html

    fastapi = types.ModuleType("fastapi")
    fastapi.FastAPI = FastAPI

    staticfiles = types.ModuleType("fastapi.staticfiles")
    staticfiles.StaticFiles = StaticFiles
    fastapi.staticfiles = staticfiles

    uvicorn = types.ModuleType("uvicorn")
    uvicorn.run = lambda *args, **kwargs: None

    sys.modules["fastapi"] = fastapi
    sys.modules["fastapi.staticfiles"] = staticfiles
    sys.modules["uvicorn"] = uvicorn

    return mounted


def test_mount_static_dir(monkeypatch):
    mounted = make_fastapi()
    if "src.serve_web" in sys.modules:
        del sys.modules["src.serve_web"]
    importlib.import_module("src.serve_web")
    assert mounted == [("/", "web", True, "static")]
