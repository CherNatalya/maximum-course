import random
import requests
from bs4 import BeautifulSoup


def get_festival():
    # присваеваем переменной response сайт
    response = requests.get('https://kudago.com/msk/festival/')
    # преобразуем его с помощью команды content, чтобы мы могли работать с содержимым сайта
    response = response.content
    # lxml - бибиотека, которая помогает структурировать данные, BeautifulSoup "собирает, видит" все теги
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='post-header'))
    print(fact.text)
    # 'href' - ссылка
    print(fact.a.attrs['href'])


def get_fact():
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    print(fact.text)
    print(fact.a.attrs['href'])


def get_concert():
    response = requests.get("https://kudago.com/msk/concerts/")
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='post-header'))
    print(fact.text)
    print(fact.a.attrs['href'])


while True:
    a = ('Выход - 0', 'Факт - 1', 'Фестиваль - 2', 'Концерт - 3')
    for i in a:
        print(i)
    n = int(input('Введите число: '))
    if n == 1:
        get_fact()
    elif n == 2:
        get_festival()
    elif n == 3:
        get_concert()
    elif n == 0:
        break
    else:
        print('Такой функции нет')
    print('-' * 60)
