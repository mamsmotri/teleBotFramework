#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dependencies
import config

bot = dependencies.telebot.TeleBot(config.token)

@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, "Goddammit")

bot.polling()