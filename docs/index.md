# Project Documentation

This page collects basic setup details and the development roadmap for the website and accompanying Telegram bot.

## Setup
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd website
   ```
2. **Create a virtual environment and install dependencies**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate  # Windows (cmd/PowerShell)
   pip install -r requirements.txt
   ```
3. **Configure environment variables**
   Copy `.env.example` to `.env` and edit the file to include your Telegram bot token:

   ```bash
   cp .env.example .env
   # open .env and set BOT_TOKEN=<your-token>
   ```
4. **Run the bot**
   ```bash
   python -m src.bot
   ```
   Website components will be added in future versions.

## Planned Features
- **Calculators**: basic arithmetic and date utilities.
- **Notes**: small note system with optional sync via the backend.
- **OS-Specific Styling**: themes tailored for desktop and mobile.
- **Telegram Integration**: access core tools directly from chat.
- **Web Backend**: APIs built with FastAPI.

## Environment Variables
- `BOT_TOKEN` – Telegram token obtained from [@BotFather](https://t.me/BotFather). Required to run the bot. Define this in a `.env` file based on `.env.example`.

## Directory Structure
```text
.
├── src/        # Application source code (bot and future backend)
├── docs/       # Documentation
├── README.md   # Project overview
├── requirements.txt
```

## Contributing
1. Fork the repository and create a new branch for your changes.
2. Install dependencies and ensure `python -m compileall -q src` succeeds.
3. Follow the existing code style and add tests for new features when applicable.
4. Open a pull request with a clear description of your changes.

