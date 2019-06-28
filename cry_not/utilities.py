import json
from requests import Request, Session


def get_telegram_bot_token():
    with open('config.json', 'r') as bot_token_file:
        data = json.load(bot_token_file)
        return data['telegramBotToken']


def get_coinmarket_api_key():
    with open('config.json', 'r') as api_key_file:
        data = json.load(api_key_file)
        return data['coinmarketApiToken']


def save_config(telegram_bot_token, coinmarket_api_key):
    with open('config.json', 'w+') as bot_token_file:
        telegram_bot_string = f'\"telegramBotToken\": \"{telegram_bot_token}\"'
        coinmarket_api_string = f'\"coinmarketApiToken\": \"{coinmarket_api_key}\"'
        json_string = '{' + telegram_bot_string + ',\n' + coinmarket_api_string + '}'
        bot_token_file.write(json_string)


def get_prices():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
