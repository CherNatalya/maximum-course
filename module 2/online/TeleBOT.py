import telebot
from random import randint, choice
import requests
from bs4 import BeautifulSoup
TOKEN = "5909185225:AAHyFbiaW6BZ_YP7DYiBTzNiH2eliCxSqtA"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(msg):  # msg - словарь с данными о пользователе который написал боту
    welcome = 'Привет, отправь мне команду'
    # создали клавиатуру
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=False)
    but_1 = telebot.types.KeyboardButton("/fact")  # создали кнопку
    but_2 = telebot.types.KeyboardButton("/poem")
    but_3 = telebot.types.KeyboardButton("/animals")
    but_4 = telebot.types.KeyboardButton("/sticker")
    but_5 = telebot.types.KeyboardButton("/music")
    but_6 = telebot.types.KeyboardButton("/game")
    but_7 = telebot.types.KeyboardButton("/back")
    keyboard.add(but_1, but_2, but_3, but_4, but_5, but_6, but_7)  # добавили кнопку в клавиатуру
    bot.send_message(msg.from_user.id, welcome, reply_markup=keyboard)  # отправили клавиатуру


@bot.message_handler(commands=['fact'])
def start(message):
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = choice(html.find_all(class_='p-2 clearfix'))
    fact_text = fact.text
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link + fact_text)


@bot.message_handler(commands=['game'])
def start(msg):
    bot.send_message(msg.from_user.id, "Выбери жанр")
    bot.send_message(msg.from_user.id, 'action' + '\n' + 'adventure' + '\n' + 'rpg' + '\n' + 'shooting' + '\n' + 'strategy' + '\n' + 'survival')
    bot.register_next_step_handler(bot.send_message(msg.from_user.id, 'Сейчас посоветую тебе игру'), games)


def games(message):
    response = requests.get('https://plarium.com/ru/games/genre/' + message.text.lower() + '-games/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    game = choice(html.find_all(class_="GameCardPromostyled__Title-sc-1f0i00l-5 cpVvei"))
    game_text = game.text
    bot.send_message(message.chat.id, game_text)


@bot.message_handler(commands=["poem"])
def start(msg):  # msg - словарь с данными о пользователе который написал боту
    text = "муха села на варенье вот и все стихотворенье"
    bot.send_message(msg.from_user.id, text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    but_url = telebot.types.InlineKeyboardButton("Перейти", url="http://my.com")
    keyboard.add(but_url)
    bot.send_message(msg.from_user.id, "больше стихов", reply_markup=keyboard)


@bot.message_handler(commands=["back"])
def start(msg):
    keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=False)
    but_5 = telebot.types.KeyboardButton("/start")
    keyboard2.add(but_5)  # добавили кнопку в клавиатуру
    bot.send_message(msg.from_user.id, "можете вернуться обратно", reply_markup=keyboard2)  # отправили клавиатуру


# https://t.me/Stickers - создание стикеров
# https://t.me/idstickerbot - узнать id стикера


@bot.message_handler(commands=["sticker"])
def start(msg):  # msg - словарь с данными о пользователе который написал боту
    id_st = 'CAACAgIAAxkBAAEG6Z1jodtuQ08m7fXFeaS8vuzTFvxQEQAC3iUAAtiNCElpiGDF7iHKfiwE'
    bot.send_sticker(msg.from_user.id, id_st)


@bot.message_handler(commands=["animals"])
def start(msg):  # msg - словарь с данными о пользователе который написал боту
    rand = randint(1, 6)
    img = open(f'img/{rand}.jpg', "rb")  # записываю файл
    bot.send_photo(msg.from_user.id, img)


@bot.message_handler(commands=["music"])
def start(msg):  # msg - словарь с данными о пользователе который написал боту
    img = open("Bones.mp3", "rb")  # записываю файл
    bot.send_audio(msg.from_user.id, img)


bot.polling()  # цикл для бота
# хочу узнать за какое время выполняется функция

# import time

# # func = main1
# def decor_time(func):
#     #улучшенная функция
#     def next_level():
#         start = time.time() #1 изменение
#         func()              #вызов функции
#         end = time.time() #2 изменение
#         print(end - start) #3 изменение
#     return next_level # вернул улучшенную функцию


# #main1 = decor_time(main1)
# @decor_time
# def main1():
#     for i in range(100):
#         print(i)


# @decor_time
# def main2():
#     for i in range(1000):
#         print(i)

# main2()


# main1 = next_level

# print() -вызов функции
# print -обьект

# x = 1
# y = x


# new_print = print
# new_print("привет")

# print = print
# print(1)


# import time
# # func = me_func
# def my_decor_time(func): # принимаю функцию которую нужно улучшить

#     def next_level(): # улучшенная функция которую я отдам обратно
#         start = time.time()  # улучшение
#         func()                     # вызов прошлой функции
#         end = time.time() # улучшение
#         result = end - start # улучшение
#         print("функция выполнилась за",  result) # улучшение

#     return next_level  #jnlf. ekexityye. aeyrwb.


# @my_decor_time
# def    my_func1():
#     for i in range(100):
#         print(1)

# @my_decor_time
# def    my_func2():
#     for i in range(1000):
#         print(1)


# # my_func1 = my_decor_time( my_func1)
# # my_func2 = my_decor_time( my_func2)

# my_func1()
# my_func2()


# x = 3
# y = x

# new_print = print
# new_print("gfyugwdfyuishwuise")
