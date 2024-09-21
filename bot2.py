from confik import token
import telebot
import random

API_TOKEN = token

bot = telebot.TeleBot(token)

jokelist = ['Шутка 1', 'Шутка 2', 'Шутка 3', 'Шутка 4']
quotelist = ['Цитата 1', 'Цитата 2', 'Цитата 3', 'Цитата 4']
factlist = ['Факт 1', 'Факт 2', 'Факт 3', 'Факт 4']

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, """Привет меня зовут MegaBot, рад буду вам помочь, я эксеприментальный
""")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """Напишите любое сообщение и я его продублирую вам в ответ""")

@bot.message_handler(commands=['joke'])
def joke(message):
    bot.reply_to(message, random.choice(jokelist))

@bot.message_handler(commands=['quote'])
def quote(message):
    bot.reply_to(message, random.choice(quotelist))

@bot.message_handler(commands=['fact'])
def fact(message):
    bot.reply_to(message, random.choice(factlist))

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()
