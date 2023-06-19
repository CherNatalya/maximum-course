import requests
from bs4 import BeautifulSoup
import contextlib
url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
xml = BeautifulSoup(response.content, 'lxml')


@contextlib.contextmanager
def get_course(my_id):
    try:
        xml1 = xml.find("valute", {'id': my_id})
        yield f"({xml1.nominal.text}шт.) {xml1.find('name').text} стоит(ят) {xml1.value.text} руб."
    except AttributeError:
        yield 'Валюта не найдена'


while True:
    with get_course(input('Введите id валюты: ')) as currency:
        print(currency)
