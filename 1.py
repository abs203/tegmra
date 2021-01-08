from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Chat
import requests
import re

bot_token = "1195318855:AAHVhMCOiQ6usUkeVMLUAIEDaE1c6elzFJ8"

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(update: Update, context: CallbackContext):
    url = get_url()
    chat_id = update.message.chat_id
    update.message.reply_photo(chat_id, url)

def send_message(update: Update, context: CallbackContext) -> None:
    print(update.message.chat.id)
    chat:Chat = context.bot.get_chat("869258827")
    chat.send_message(update.message.text)
    
def send_sticker(update: Update, context: CallbackContext) -> None:
    chat:Chat = context.bot.get_chat("869258827")
    chat.send_sticker(update.message.sticker)

def send_photo(update: Update, context: CallbackContext) -> None:
    chat:Chat = context.bot.get_chat("869258827")
    chat.send_photo(update.message.photo[0])

def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_message))
    dp.add_handler(MessageHandler(Filters.sticker & ~Filters.command, send_sticker))
    dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, send_photo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
