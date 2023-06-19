name = input('Введите имя: ')
age = int(input('Введите возраст: '))
city = input('Введите город: ')
year = 0
if age % 100 < 10 or age % 100 > 14:
    if age % 10 == 1:
        year = 'год'
    elif 2 <= age % 10 <= 4:
        year = 'года'
    else:
        year = 'лет'
else:
    year = 'лет'
print('Меня зовут', name, 'я из города', city, 'мне', age, year)
