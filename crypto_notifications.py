import os
import sys
import requests
from cry_not import utilities


def main():
    if 'config.json' not in os.listdir(os.getcwd()):
        telegram_bot_token = input('Please enter your Telegram bot token:\n')
        telegram_chat_id = input('Please enter your Telegram chat ID:\n')
        coinmarket_api_key = input('Please enter your Coinmarket API key:\n')
        utilities.save_config(telegram_bot_token, telegram_chat_id, coinmarket_api_key)

    telegram_bot_token = utilities.get_telegram_bot_token()
    coinmarket_api_key = utilities.get_coinmarket_api_key()
    telegram_chat_id = utilities.get_telegram_chat_id()
    bitcoin_price = utilities.get_prices(coinmarket_api_key)
    utilities.send_prices(telegram_bot_token, telegram_chat_id, bitcoin_price)


if __name__ == '__main__':
    main()
