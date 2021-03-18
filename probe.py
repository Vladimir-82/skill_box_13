import requests
import telebot
from token_telegram import _token
bot = telebot.TeleBot(_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться,{message.from_user.first_name}')

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # if message.text.lower() == 'привет':
    #     bot.send_message(message.from_user.id, 'Привет!')
    # elif message.text.lower() == 'жыве беларусь':
    #     bot.send_message(message.from_user.id, 'Жыве вечна!')
    # elif 'лукашенко' in message.text.lower().split():
    #     bot.send_message(message.from_user.id, 'хай здохне')
    inq = message.text
    responce = requests.get('http://ru.wikipedia.org/wiki' + '/' + str(inq))

    if inq in responce.text:
        bot.send_message(message.from_user.id, responce.text[responce.text.index('<title>') + len('<title>'):responce.text.index('</title>')])

        var = responce.text[responce.text.index('<p>') + len('<p>'):responce.text.index('</p>')]
        var_exit = list(var)
        while "<" in var_exit:
            del var_exit[var_exit.index('<'):var_exit.index('>') + 1]

        while "&#160;" in var_exit:
            del var_exit[var_exit.index("&#160;"):var_exit.index("&#160;") + len("&#160;")]

        while "&#91;1&#93;" in var_exit:
            del var_exit[var_exit.index("&#91;1&#93;"):var_exit.index("&#91;1&#93;") + len("&#91;1&#93;")]

        bot.send_message(message.from_user.id, ''.join(var_exit))
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, тебя, дружище!')
bot.polling(none_stop = True)
