# Cryptocurrency Notifier

This is a simple bot that texts a user the price of any cryptocurrency every hour. Built in Python 3, this project uses the `requests` package to query [Coinmarket Cap's API](https://coinmarketcap.com/api/documentation/v1/) about the price of the given currency and then sends that information to the user through a Telegram bot using the [Telegram Bot API](https://core.telegram.org/bots/api). This bot uses `pipenv` as its virtual environment.

## Installation
>Requires Python 3.0 or higher

A few steps are required in order to get this bot working. Firstly, clone this git repo by running the following in your terminal:

`$ cd path/to/clone/in`

`$ git clone https://github.com/aliu2/crypto_notifications.git`

Now that you have the repository cloned, you'll need a few things to configure the bot:
- A Telegram Bot and a Bot Token (you can find how to create one [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot)).
- An API key from Coinmarket Cap ([create an account](https://pro.coinmarketcap.com/signup) to receive your personal key)
- The chat ID for the particular chat you want to interact with your bot in, whether that be a personal DM or a group chat.

In order to obtain your chat ID, first create the Telegram chat bot and obtain your Bot Token (link above). Then, send it a nice greeting! Not just to be polite but also because you need to obtain the chat ID for the chat you want to interact with your bot in. 

Once you've sent your bot a quick text, copy and paste this URL into the address bar of any browser:

`https://api.telegram.org/bot<bot token>/getUpdates`

Be sure to replace `<bot token>` with your bot's token.

This request will return a JSON object containing information about any updates to your bot (more on that [here](https://core.telegram.org/bots/api#update)). What you're looking for in this JSON object is the 'id' field. The value for this field is your chat ID. Tuck it away somewhere safe!

In order to configure the bot, run it once inside of its virtual environment. To do this, enter the following commands into your terminal:

_Change directory into the project_

`$ cd location/of/crypto_notifications`

_Activate the virtual environment_

`$ pipenv shell`

_Run the main program_

`$ python3 crypto_notifications.py`

Now, the first time you run this python bot, you'll be asked for three things:
- Your Telegram bot's bot token
- The chat ID for the chat you wish to interact with the bot in
- Your Coinmarket API key

All in that order. Input these fields one by one when prompted to configure the python bot. Check your Telegram app, you should receive a text from your bot with a little cryptocurrency price update!

## Scheduling
This program can be scheduled to be run every hour on any Unix operating system through the use of `cron`, which is a time-based job scheduler available on all Unix machines. 

Firstly, hop into your terminal and run the following command to get a list of your current cron jobs:

`$ crontab -l`

If you've never used cron before, this command will inform you that there are no crontabs for this user, otherwise it'll give you a list of your current cron jobs.

To add a cron job that runs this python program once every hour, enter this command to edit your list of cron jobs:

`$ crontab -e`

Then, enter the following line to schedule this python program (all paths must be absolute paths):

`0 * * * * cd /location/of/crypto_notifications && /location/of/python3 crypto_notifications.py`

This tells cron to change directory into the project directory and run the main program using python3, and to do this on the 0th minute of every hour of every day of the month, every month, every day of the week. Or, to put it simple, every hour!
