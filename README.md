# Multipurpose Website and Bot

This repository contains the early foundation for a cross-platform website bundled with a Telegram bot. The goal is to provide handy utilities such as calculators and a lightweight note system. The site will adapt its styling for different operating systems to feel native whether viewed on Windows, macOS, Linux, or mobile devices.

## Purpose
- Offer quick-access calculators for everyday use.
- Allow users to create and manage personal notes.
- Provide a consistent look and feel across platforms with OS-aware themes.
- Expose certain features through an accompanying Telegram bot.

## Expected Features
- **Calculators**: basic arithmetic, date calculations, and other small tools.
- **Notes**: simple note-taking with the ability to sync via the backend.
- **OS-Specific Styling**: themes optimized for desktop and mobile operating systems.
- **Telegram Integration**: chat-based access to calculators and notes through the bot.

## Target Platforms
- Desktop browsers (Windows, macOS, Linux)
- Mobile browsers (Android, iOS)
- Telegram clients

## Project Roadmap
1. Establish project structure and continuous integration.
2. Implement core calculator components.
3. Introduce note management backend and UI.
4. Apply OS-specific themes and responsive layout.
5. Integrate Telegram bot with website features.
6. Prepare deployment workflow and documentation.

## High-Level Architecture
- **Frontend**: Static pages enhanced with JavaScript for interactivity. Styling layers apply platform-specific themes.
- **Backend**: Python service (planned with FastAPI) providing APIs for calculators and notes. The same service hosts the aiogram-based Telegram bot.
- **Data Storage**: Lightweight database (such as SQLite) for notes and user data.
- **Deployment**: Containerized application ready for hosting on common cloud providers.

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
   source .venv/bin/activate  # Linux/macOS
   .\.venv\Scripts\activate  # Windows (cmd/PowerShell)
   pip install -r requirements.txt
   ```
3. **Set the bot token**
   Export your token as an environment variable:

   **Unix/macOS**
   ```bash
   export BOT_TOKEN=<your-token-here>
   ```

   **Windows (Command Prompt)**
   ```cmd
   set BOT_TOKEN=<your-token>
   ```

   **Windows (PowerShell)**
   ```powershell
   $env:BOT_TOKEN="<your-token>"
   ```
4. **Run the bot**
   ```bash
   python -m src.bot
   ```
   Run this command from the directory that contains the `src/` and `web/` folders (the repository root).

## Project Structure
```
.
├── src/        # Application source code (Telegram bot and future backend)
├── web/        # Static HTML and CSS
├── docs/       # Project documentation
├── README.md   # This file
└── requirements.txt
```

## Serving the Web Interface Locally

You can preview the static pages using a small FastAPI application.

1. **Install additional dependencies**
   ```bash
   pip install fastapi uvicorn
   ```
2. **Run the server**
   ```bash
   python -m src.serve_web
   ```
   Run this command from the same directory that contains the `src/` and `web/` folders. Then open `http://127.0.0.1:8000` in your browser.

## License
This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for details.
