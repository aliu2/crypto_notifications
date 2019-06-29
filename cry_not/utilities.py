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


# TODO:
#   1. Get coinmarket api key
#   2. Insert api key into request header
#   3. Make requests
def get_prices(coinmarket_api_key):
    coinmarket_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'id': '1',
        'convert': 'EUR'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': coinmarket_api_key,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(coinmarket_api_url, params=parameters)
    data = json.loads(response.text)
    return data['data']['1']['quote']['EUR']['price']
