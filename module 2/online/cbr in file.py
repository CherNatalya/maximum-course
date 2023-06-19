import requests
from bs4 import BeautifulSoup
import datetime
url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.datetime.today()
today = today.strftime('%d/%m/%Y')
date = f'date_req={today}'
response = requests.get(url+date)
xml = BeautifulSoup(response.content, 'lxml')
file1 = open("values.txt", "w")


def get_course(my_id):
    xml1 = xml.find("valute", {'id': my_id})
    return {"value": xml1.value.text, "nominal": xml1.nominal.text, "name": xml1.charcode.text}


for val_code in ['R01235', 'R01239', 'R01375', 'R01215', 'R01720', 'R01815', 'R01335']:
    temp_dict = get_course(val_code)
    op = f'{round(float(temp_dict["value"].replace(",", ".")), 2)} рублей за {temp_dict["nominal"]} {temp_dict["name"]}'
    print(op)
    file1.write(op + '\n')
file1.close()
