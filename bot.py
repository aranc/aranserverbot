from twx.botapi import TelegramBot, ReplyKeyboardMarkup
import os

with open(os.path.expanduser("~/aranserverbot"), 'r') as _file:
    api_token = _file.readline()

print api_token
