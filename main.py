#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dependencies import *
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, "Goddammit")

bot.polling()