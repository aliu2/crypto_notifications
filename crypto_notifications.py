import os
import sys
import requests
from cry_not import utilities
# https://api.telegram.org/bot<token>/METHOD_NAME

# bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
# response = requests.get(bitcoin_api_url)
# response_json = response.json()
# print(type(response_json))
# print(response_json[0])


def main():
    if 'bot_token.json' not in os.listdir(os.getcwd()):
        bot_token = input('Please enter your Telegram bot token:\n')
        utilities.save_bot_token(bot_token)
    # utilities.get_bot_token()


if __name__ == '__main__':
    main()
