import requests
import telebot
from token_telegram import _token
bot = telebot.TeleBot(_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться,{message.from_user.first_name}')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # if message.text.lower() == 'привет':
    #     bot.send_message(message.from_user.id, 'Привет!')
    # elif message.text.lower() == 'жыве беларусь':
    #     bot.send_message(message.from_user.id, 'Жыве вечна!')
    # elif 'лукашенко' in message.text.lower().split():
    #     bot.send_message(message.from_user.id, 'хай здохне')
    res = 'добро'
    responce = requests.get('http://ru.wikipedia.org')

    if res in message.text.lower():
        bot.send_message(message.from_user.id, responce.text)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, тебя, дружище!')
bot.polling(none_stop = True)
