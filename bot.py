import os
from telegram import Bot

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["8339097197"]

BOT = Bot(token=TOKEN)

# testowa wiadomość
BOT.send_message(chat_id=CHAT_ID, text="✅ Bot działa!")
