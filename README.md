# Telegram Bot Skeleton

This repository provides a minimal structure for a Telegram bot project built with [aiogram](https://github.com/aiogram/aiogram).

## Requirements
- Python 3.9+
- A Telegram bot token obtained from [@BotFather](https://t.me/BotFather)

## Setup
1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd website
   ```
2. **Create a virtual environment and install dependencies**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Set the bot token**
   Export your token as an environment variable:
   ```bash
   export BOT_TOKEN=<your-token-here>
   ```
4. **Run the bot**
   ```bash
   python -m src.bot
   ```

## Project Structure
```
.
├── src/        # Application source code
├── docs/       # Project documentation
├── README.md   # This file
└── requirements.txt
```

## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.
