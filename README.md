# CCXT Binance Trading Bot

This repository provides a simple cryptocurrency trading bot using the **CCXT** library on Binance.

## What is CCXT?
**CCXT (CryptoCurrency eXchange Trading Library)** is a popular open-source library for connecting and trading on multiple cryptocurrency exchanges using a unified API.

## Features of This Bot
✅ Fetches real-time BTC/USDT prices using CCXT  
✅ Places buy orders when the price drops below a threshold  
✅ Places sell orders when the price rises above a threshold  
✅ Dockerized for easy deployment  

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ccxt-binance-bot.git
   cd ccxt-binance-bot
   ```

## Usage
1. **Update Your API Keys** in `ccxt_binance_bot.py`:
   ```python
   API_KEY = 'your_api_key'
   API_SECRET = 'your_api_secret'
   ```
2. **Run the Bot**:
   ```bash
   python ccxt_binance_bot.py
   ```

## About CCXT
CCXT supports over 100 cryptocurrency exchanges and allows for:  
🔹 Fetching market data  
🔹 Placing and managing orders  
🔹 Handling authentication securely  

For more details, check the **[CCXT Documentation](https://github.com/ccxt/ccxt)**.

## Contributing
Feel free to fork the repo, submit issues, or contribute improvements! 🚀

## License
This project is licensed under the MIT License.
