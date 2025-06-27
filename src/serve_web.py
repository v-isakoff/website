"""Serve the static web directory using FastAPI."""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional dependency
    def load_dotenv(*args, **kwargs):
        return False

load_dotenv()
app = FastAPI()
app.mount("/", StaticFiles(directory="web", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
