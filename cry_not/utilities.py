import json


def get_bot_token():
    with open('bot_token.json', 'r') as bot_token_file:
        data = json.load(bot_token_file)
        print(data['botToken'])
