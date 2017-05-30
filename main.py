#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dependencies import *
import config



bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Это не суть, что я вижу")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "это /help")

bot.polling()