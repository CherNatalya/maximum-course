import telebot
from random import choice
import requests
from bs4 import BeautifulSoup
token = '5657615722:AAEnJ1wSNQPWKnXNCA-5rhnCi5YzIaXklG0'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['fact'])
def get_fact(message):
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = choice(html.find_all(class_='p-2 clearfix'))
    fact_text = fact.text
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link + fact_text)


@bot.message_handler(commands=['concert'])
def get_concert(message):
    send = bot.send_message(message.chat.id, 'Напиши свой город')
    bot.register_next_step_handler(send, concerts)


def concerts(message):
    if message.text.lower() == 'москва':
        response = requests.get("https://kudago.com/msk/concerts/")
    elif message.text.lower() == 'санкт-петербург':
        response = requests.get("https://kudago.com/spb/concerts/")
    elif message.text.lower() == 'казань':
        response = requests.get("https://kzn.kudago.com/concerts/")
    elif message.text.lower() == 'новосибирск':
        response = requests.get("https://nsk.kudago.com/concerts/")
    elif message.text.lower() == 'екатеринбург':
        response = requests.get("https://ekb.kudago.com/concerts/")
    elif message.text.lower() == 'нижний новгород':
        response = requests.get("https://nn.kudago.com/concerts/")
    elif message.text.lower() == 'красноярск':
        response = requests.get("https://krasnoyarsk.kudago.com/concerts/")
    elif message.text.lower() == 'краснодар':
        response = requests.get("https://krd.kudago.com/concerts/")
    elif message.text.lower() == 'сочи':
        response = requests.get("https://sochi.kudago.com/concerts/")
    elif message.text.lower() == 'минск':
        response = requests.get("https://minsk.kudago.com/concerts/")
    else:
        bot.send_message(message.chat.id, 'Такого города я ещё не знаю, либо вы неправильно ввели название =(')
        bot.send_message(message.chat.id, 'Посоветую тебе онлайн-мероприятие)')
        response = requests.get("https://online.kudago.com/online-events/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    concert = choice(html.find_all(class_='post-header'))
    concert_text = concert.text
    concert_link = concert.a.attrs['href']
    bot.send_message(message.chat.id, concert_link + concert_text)


@bot.message_handler(commands=['exhibition'])
def get_exhibition(message):
    send = bot.send_message(message.chat.id, 'Напиши свой город')
    bot.register_next_step_handler(send, exhibitions)


def exhibitions(message):
    if message.text.lower() == 'москва':
        response = requests.get("https://kudago.com/msk/exhibitions/")
    elif message.text.lower() == 'санкт-петербург':
        response = requests.get("https://kudago.com/spb/exhibitions/")
    elif message.text.lower() == 'казань':
        response = requests.get("https://kzn.kudago.com/exhibitions/")
    elif message.text.lower() == 'новосибирск':
        response = requests.get("https://nsk.kudago.com/exhibitions/")
    elif message.text.lower() == 'екатеринбург':
        response = requests.get("https://ekb.kudago.com/exhibitions/")
    elif message.text.lower() == 'нижний новгород':
        response = requests.get("https://nn.kudago.com/exhibitions/")
    elif message.text.lower() == 'красноярск':
        response = requests.get("https://krasnoyarsk.kudago.com/exhibitions/")
    elif message.text.lower() == 'краснодар':
        response = requests.get("https://krd.kudago.com/exhibitions/")
    elif message.text.lower() == 'сочи':
        response = requests.get("https://sochi.kudago.com/exhibitions/")
    elif message.text.lower() == 'минск':
        response = requests.get("https://minsk.kudago.com/exhibitions/")
    else:
        bot.send_message(message.chat.id, 'Такого города я ещё не знаю, либо вы неправильно ввели название =(')
        bot.send_message(message.chat.id, 'Посоветую тебе онлайн-мероприятие)')
        response = requests.get("https://online.kudago.com/online-events/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    exhibition = choice(html.find_all(class_='post-header'))
    exhibition_text = exhibition.text
    exhibition_link = exhibition.a.attrs['href']
    bot.send_message(message.chat.id, exhibition_link + exhibition_text)


@bot.message_handler(commands=['kino'])
def get_kino(message):
    response = requests.get("https://kudago.com/msk/kino/schedule-cinema/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    movie = choice(html.find_all(class_='post-header'))
    movie_text = movie.text
    movie_link = movie.a.attrs['href']
    bot.send_message(message.chat.id, movie_link + movie_text)


@bot.message_handler(commands=['test'])
def get_test(message):
    response = requests.get("https://testometrika.com/tests/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    tests = choice(html.find_all(class_='col-xs-12 col-sm-6'))
    tests_text = tests.find(class_='test-list__test__title').text.lstrip()
    tests_link = 'https://testometrika.com' + tests.a.attrs['href']
    bot.send_message(message.chat.id, tests_link + '\n' + tests_text)


@bot.message_handler(commands=['poem'])
def get_poem(message):
    response = requests.get("https://rustih.ru/stihi-russkih-poetov-klassikov/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    poems = choice(html.find_all(class_='entry-title'))
    poems_text = poems.text
    poems_link = poems.a.attrs['href']
    bot.send_message(message.chat.id, poems_link + '\n' + poems_text)


@bot.message_handler(commands=['book'])
def get_book(message):
    bot.send_message(message.chat.id, 'Пожалуйста, подожди буквально секунду)')
    response = requests.get("https://www.litmir.me/bs/?rs=5%7C1%7C0")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    books = choice(html.find_all(class_='book_name'))
    books_text = books.text
    books_link = books.a.attrs['href']
    bot.send_message(message.chat.id, 'https://www.litmir.me' + books_link + '\n' + books_text)


@bot.message_handler(commands=['film'])
def get_film(message):
    bot.send_message(message.chat.id, 'Пожалуйста, подожди буквально секунду)')
    response = requests.get("https://kino.mail.ru/cinema/all/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fil = choice(html.find_all(class_="text text_block text_fixed text_light_large"))
    film_text = fil.text
    film_link = fil.a.attrs['href']
    bot.send_message(message.chat.id, 'https://kino.mail.ru/' + film_link + '\n' + film_text)


@bot.message_handler(content_types=['text'])
def text_message(message):
    hi = ['Hello)', 'Здравствуй', 'Салют!', 'Бонжур', 'Hi', 'Привет =)']
    hru = ['Хорошо', 'Всё отлично', 'Прекрасно, надеюсь, у тебя тоже)', 'Неплохо =)']
    act = ['Почитай книгу, могу посоветовать', 'Посмотри фильм, могу посоветовать', 'Порисуй', 'Поиграй во что-нибудь']
    thanks = ['Всегда пожалуйста', 'Не за что)', 'Пожалуйста =)', 'Без проблем', 'Рад помочь', 'Обращайся']
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, choice(hi))
    elif message.text.lower() == 'как дела?' or message.text.lower() == 'как дела':
        bot.send_message(message.from_user.id, choice(hru))
    elif message.text.lower() == 'мне грустно' or message.text.lower() == 'развесели меня':
        c = choice(['Cat.jpg', 'Cat2.jpg', 'Bird.jpg', 'Dog.jpg', 'Hedg.jpg', 'Hedg2.jpg', 'Owl.jpg', 'Owl2.jpg'])
        bot.send_photo(message.from_user.id, open(c, 'rb'))
    elif message.text.lower() == 'чем мне заняться?' or message.text.lower() == 'мне скучно':
        bot.send_message(message.from_user.id, choice(act))
    elif message.text.lower() == 'спасибо':
        bot.send_message(message.from_user.id, choice(thanks))


bot.polling()
