# Binance Futures Trading Bot

A simplified Python trading bot for Binance Futures with CLI support, validation, structured logging, and error handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- CLI-based order execution
- Input validation
- Structured logging
- Exception handling
- Modular architecture

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── .env
├── README.md
└── requirements.txt

---

## Setup

### Create Virtual Environment

```bash
python -m venv venv