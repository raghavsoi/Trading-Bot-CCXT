import ccxt
import time

# Replace with your Binance API keys
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

# Initialize Binance exchange
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'options': {'defaultType': 'spot'}
})

def get_price(symbol='BTC/USDT'):
    """Fetches the latest market price of the given symbol."""
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def place_order(symbol, side, amount):
    """Places a market order on Binance."""
    order = exchange.create_market_order(symbol, side, amount)
    return order

# Simple trading logic
symbol = 'BTC/USDT'
buy_price = 40000  # Set your buy threshold
sell_price = 42000  # Set your sell threshold
trade_amount = 0.001  # Amount to trade

while True:
    try:
        price = get_price(symbol)
        print(f'Current {symbol} Price: {price}')
        
        if price < buy_price:
            print('Buying...')
            place_order(symbol, 'buy', trade_amount)
        elif price > sell_price:
            print('Selling...')
            place_order(symbol, 'sell', trade_amount)
        
        time.sleep(10)  # Wait before checking again
    except Exception as e:
        print(f'Error: {e}')
        time.sleep(10)