import requests
from bs4 import BeautifulSoup
response = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
response = response.content
html = BeautifulSoup(response, 'lxml')
devices = html.find_all(class_='row ecomerce-items ecomerce-items-ajax')
print(devices[0]['data-items'])
