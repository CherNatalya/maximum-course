import requests
from bs4 import BeautifulSoup
import datetime
url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.datetime.today()
today = today.strftime('%d/%m/%Y')
date = f'date_req={today}'
response = requests.get(url+date)
xml = BeautifulSoup(response.content, 'lxml')


def course(valute_from, valute_to, amount):
    nominal = 0
    value = 0
    amount1 = 0
    if valute_to == valute_from:
        return str(amount) + ' ' + valute_from + ' - ' + str(amount) + ' ' + valute_to
    if valute_to == 'RUR':
        nominal = 1
        value = 1
    elif valute_from == 'RUR':
        amount1 = amount
    for n in xml.find_all('valute'):
        if n.charcode.text == valute_from:
            amount1 = float(n.value.text.replace(',', '.')) * amount / float(n.nominal.text)
        elif n.charcode.text == valute_to:
            nominal = float(n.nominal.text)
            value = float(n.value.text.replace(',', '.'))
    if amount1 == 0 or nominal == 0:
        return 'Неверная валюта'
    return str(amount) + ' ' + valute_from + ' - ' + str(round(nominal * amount1 / value, 4)) + ' ' + valute_to


print(course('EUR', 'USD', int(input('Введите сумму: '))))
print(course(input('Введите 1 валюту: '), input('Введите 2 валюту: '), int(input('Введите сумму: '))))
