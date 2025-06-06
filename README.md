# Telegram Bot Creator Platform

A platform that allows users to create and manage their own Telegram bots with various AI capabilities.

## Features

- Create and manage multiple Telegram bots
- Web interface for bot management
- Support for various AI models (GPT, Claude, Gemini)
- Bot customization and analytics
- Monetization options

## Tech Stack

- Python 3.9+
- FastAPI for web interface
- SQLAlchemy for database
- Python-telegram-bot for bot functionality
- PostgreSQL for data storage

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your configuration (see `.env.example`)
5. Run the application:
   ```bash
   python main.py
   ```

## Project Structure

```
├── app/
│   ├── bot/           # Bot-related code
│   ├── web/           # Web interface
│   ├── core/          # Core functionality
│   └── models/        # Database models
├── alembic/           # Database migrations
├── tests/             # Test files
└── docs/              # Documentation
```

## License

MIT License 