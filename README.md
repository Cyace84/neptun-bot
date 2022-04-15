# neptun-bot
DDOS of separatist bot

# Requirements
- Installed Python3+
- Installed Python requirements:
To install requirements type in terminal
```
pip3 install -r requirements.txt
```

# How start
The configuration file is already configured, but if you wish, you can change the settings in the bot.cfg file, namely:
- spam_count - How many messages will the bot send
- chat_id - Target bot username. As soon as the target is eliminated, you need to replace it with a new username
- text - The message that the bot will send
- api_id and api_hash - These are special keys for using the telegram API, you can get it here my.telegram.org. But this is not necessary, you can use those that are already installed.

To start the bot, enter in the terminal:

On the first launch, you will need to enter a phone number and a verification code. The bot does not save your phone, this is necessary for the telegram API, more details https://docs.pyrogram.org/intro/quickstart

```
python3 run.py
```

# How Stop

```
ctrl(^) + с
```
or close your terminal


# Very important! Do not use the bot to send messages to ordinary users - your account will be blocked by telegram very quickly.

# Plase use the development reasonably without violating the laws of Ukraine. Only for the destruction of muscovites-bots.
# Слава Україні 🇺🇦
