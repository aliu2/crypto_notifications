import json
import requests


def get_telegram_bot_token():
    with open('tokens.json', 'r') as bot_token_file:
        data = json.load(bot_token_file)
        print(data['telegramBotToken'])


def save_config(telegram_bot_token, coinmarket_api_key):
    with open('tokens.json', 'w+') as bot_token_file:
        telegram_bot_string = f'\"telegramBotToken\": \"{telegram_bot_token}\"'
        coinmarket_api_string = f'\"coinmarketApiToken\": \"{coinmarket_api_key}\"'
        json_string = '{' + telegram_bot_string + ',\n' + coinmarket_api_string + '}'
        bot_token_file.write(json_string)


def get_prices():
    bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/1027/'
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    print(response_json[0])
