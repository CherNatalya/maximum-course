''' hour = 10
if 5 <= hour <= 10:
    print("Сейчас утро")
elif 11 <= hour <= 16:
    print("Сейчас день")
elif 17 <= hour <= 22:
    print("Сейчас вечер")
elif 23 <= hour <= 4:
    print("Сейчас день")


class Person:
    def __init__(self, age, sex, weight, height, is_college, is_high_grade):
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height
        self.is_college = is_college
        self.is_high_grade = is_high_grade

    def print_info(self):
        if self.age >= 14:
            if self.sex == 'w':
                print('У неё есть паспорт')
            elif self.sex == 'm':
                print('У него есть паспорт')
        else:
            if self.sex == 'w':
                print('У неё нет паспорта')
            elif self.sex == 'm':
                print('У него ytn паспорта')
        if self.age >= 15 and self.is_college:
            if self.sex == 'w':
                print('Пошла в колледж после школы')
            elif self.sex == 'm':
                print('Пошёл в колледж после школы')
        elif self.age >= 17 and self.is_high_grade:
            if self.sex == 'w':
                print('Пошла в вуз')
            elif self.sex == 'm':
                print('Пошёл в вуз')


nata = Person(15, 'w', 45, 161, False, False)
nata.print_info() '''

import requests
url = 'https://rickandmortyapi.com/api/'
response = requests.get(url).json()
ep_link = response['episodes']
ep_input = int(input('Введите номер эпизода: '))
response = requests.get(f"{ep_link}/{ep_input}").json()
translation_dict = {
    'Rick Sanchez': "Рик Санчез"
}
for char_link in response['characters']:
    response = requests.get(char_link).json()
    if response['name'] in translation_dict.keys():
        print(translation_dict[response['name']])
    else:
        print(response['name'])
