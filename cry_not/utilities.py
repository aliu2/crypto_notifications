import json


def get_bot_token():
    with open('bot_token.json', 'r') as bot_token_file:
        data = json.load(bot_token_file)
        print(data['botToken'])


def save_bot_token(bot_token):
    with open('bot_token.json', 'w+') as bot_token_file:
        bot_token_string = '{\"botToken\": \"' + bot_token + '\"}'
        bot_token_file.write(bot_token_string)
