# Mr. Cat

A simple Telegram bot built with Python (`aiogram`) that sends random cat pictures using [The Cat API](https://thecatapi.com/).

## Commands
* `/start` - Greeting and instructions.
* `/cat` - Get a random cat picture.

## Setup & Run

Copy the example environment file and fill in your keys:
```bash
cp .env.example .env
```

2. **Run with Docker (Recommended):**
```bash
docker-compose up -d --build
```

3. **Or run locally** (using `uv` or `pip`):
```bash
uv run bot.py
```
