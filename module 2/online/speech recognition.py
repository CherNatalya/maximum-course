import pyaudio
import requests
from bs4 import BeautifulSoup
from random import choice
import speech_recognition as sr
r = sr.Recognizer()
greets = ['Привет', 'Здравствуй)', 'Hi', 'Hello', 'Приветик', 'Салют!', 'Хай :)', 'Hola', 'Салам', 'Чао', 'Бонжур']


def get_poem():
    response = requests.get("https://rustih.ru/stihi-russkih-poetov-klassikov/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    poems = choice(html.find_all(class_='entry-title'))
    return poems.text, poems.a.attrs['href']


def get_film():
    response = requests.get("https://kino.mail.ru/cinema/all/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    film = choice(html.find_all(class_="text text_block text_fixed text_light_large"))
    return film.a.attrs['href'], film.text


def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = choice(html.find_all(class_='p-2 clearfix'))
    return fact.a.attrs['href'], fact.text


def get_kino():
    response = requests.get("https://kudago.com/msk/kino/schedule-cinema/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    movie = choice(html.find_all(class_='post-header'))
    return movie.text, movie.a.attrs['href']


def get_test():
    response = requests.get("https://testometrika.com/tests/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    tests = choice(html.find_all(class_='col-xs-12 col-sm-6'))
    return tests.find(class_='test-list__test__title').text.lstrip(), 'https://testometrika.com' + tests.a.attrs['href']


while True:
    with sr.Microphone(device_index=1) as source:
        print('Скажи что-нибудь... ')
        audio = r.listen(source)
    speech = r.recognize_google(audio, language='ru_RU').lower()
    if speech == 'привет':
        print(choice(greets))
    elif speech == 'фильм':
        print('https://kino.mail.ru/', end='')
        print(*get_film(), sep='\n')
    elif speech == 'факт':
        print(*get_fact())
    elif speech == 'кино':
        print(*get_kino())
    elif speech == 'тест':
        print(*get_test())
    elif speech == 'стих':
        print(*get_poem())
    elif speech == 'я тебя люблю':
        print('Я тебя тоже)')
    elif speech == 'спасибо':
        print('Всегда рад помочь')
    elif speech == 'пока':
        print('До скорого :)')
        break
    print(f"Вы сказали: {speech}")
