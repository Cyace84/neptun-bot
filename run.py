from pyrogram import Client
from random import randint
from time import sleep
from configparser import ConfigParser

BOT_CFG = 'bot.cfg'
parser = ConfigParser()
parser.read(BOT_CFG)
cfg = parser["config"]

spam_interval = randint(1, 8)

app = Client('session', api_id=cfg["api_id"], api_hash=cfg["api_hash"])

with app:
    print("Підпалюємо москву...")
    app.send_message(cfg["chat_id"], "/start")

    for i in range(int(cfg["spam_count"])):
        app.send_message(cfg["chat_id"], cfg["text"])
        sleep(spam_interval)

if __name__ == "__main__":
    app.run()
