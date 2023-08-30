import os
import requests
import telebot

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome!")


@bot.message_handler(func=lambda m: True)
def send_response(message):
    text = message.text
    payload = {'text': text}
    r = requests.post('http://model_service:5000/predict', json=payload)
    bot.reply_to(message, r.json()['response'])


bot.polling()
