t = int(input('Введите температуру на улице: '))
if t < -20:
    print('Очень холодно')
elif -20 <= t < 0:
    print('Холодно')
elif 0 <= t < 15:
    print('Прохладно')
elif 15 <= t < 25:
    print('Тепло')
elif 25 <= t < 40:
    print('Жарко')
else:
    print('Очень жарко')
