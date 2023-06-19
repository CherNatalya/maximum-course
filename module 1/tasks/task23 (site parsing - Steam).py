import requests
import random
from bs4 import BeautifulSoup
List = []
response = requests.get('https://store.steampowered.com/tags/ru/Экшен/')
response = response.content
html = BeautifulSoup(response, 'lxml')
game = html.find_all()
print(game)
