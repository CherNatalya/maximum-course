from random import choice, randint
import requests
from bs4 import BeautifulSoup
g = input('Выбери жанр:' + '\n' + 'action' + '\n' + 'adventure' + '\n' + 'rpg' + '\n' + 'shooting' + '\n' + 'strategy' + '\n' + 'survival' + '\n')
response = requests.get('https://plarium.com/ru/games/genre/' + g.lower() + '-games/')
response = response.content
html = BeautifulSoup(response, 'lxml')
game = choice(html.find_all(class_="GameCardPromostyled__Title-sc-1f0i00l-5 cpVvei"))
game_text = game.text
print(game_text)
