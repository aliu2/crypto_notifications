import json
import requests


def get_telegram_bot_token():
    with open('config.json', 'r') as bot_token_file:
        data = json.load(bot_token_file)
        return data['telegramBotToken']


def get_telegram_chat_id():
    with open('config.json', 'r') as chat_id_file:
        data = json.load(chat_id_file)
        return data['chatId']


def get_coinmarket_api_key():
    with open('config.json', 'r') as api_key_file:
        data = json.load(api_key_file)
        return data['coinmarketApiToken']


def save_config(telegram_bot_token, telegram_chat_id, coinmarket_api_key):
    with open('config.json', 'w+') as bot_token_file:
        telegram_bot_string = f'\"telegramBotToken\": \"{telegram_bot_token}\"'
        telegram_chat_id = f'\"chatId\": \"{telegram_chat_id}\"'
        coinmarket_api_string = f'\"coinmarketApiToken\": \"{coinmarket_api_key}\"'
        json_string = '{' + telegram_bot_string + ',\n' + telegram_chat_id + ', \n' + coinmarket_api_string + '}'
        bot_token_file.write(json_string)


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

    session = requests.Session()
    session.headers.update(headers)

    response = session.get(coinmarket_api_url, params=parameters)
    data = json.loads(response.text)
    return data['data']['1']['quote']['EUR']['price']


def send_prices(telegram_bot_token, chat_id, price):
    text = f'Bitcoin price: {price}'
    telegram_api_url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'

    parameters = {
        'chat_id': chat_id,
        'text': text
    }

    requests.get(telegram_api_url, params=parameters)
