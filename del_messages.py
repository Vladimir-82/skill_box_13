import requests
import telebot
from telebot import apihelper

from token_telegram import _token

bot = telebot.TeleBot(_token)

def delete_message(self, chat_id, message_id):

    return apihelper.delete_message(self.token, chat_id, message_id)


bot.polling(none_stop=True)
