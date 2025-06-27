"""Top-level package for the multipurpose website and bot."""

from .bot import dp, main

try:
    from .serve_web import app
except Exception:  # pragma: no cover - web is optional
    app = None

__all__ = ["dp", "main", "app"]
