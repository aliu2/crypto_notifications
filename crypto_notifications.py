import os
import sys
import requests
from cry_not import utilities
# https://api.telegram.org/bot<token>/METHOD_NAME


def main():
    if 'config.json' not in os.listdir(os.getcwd()):
        telegram_bot_token = input('Please enter your Telegram bot token:\n')
        coinmarket_api_key = input('Please enter your Coinmarket API key:\n')
        utilities.save_config(telegram_bot_token, coinmarket_api_key)
    # utilities.get_bot_token()

    telegram_bot_token = utilities.get_telegram_bot_token()
    coinmarket_api_key = utilities.get_coinmarket_api_key()
    print(telegram_bot_token)
    print(coinmarket_api_key)
    # bitcoin_price = utilities.get_prices()


if __name__ == '__main__':
    main()
