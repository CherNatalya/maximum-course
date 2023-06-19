def greeting():
    print('Привет!')
    print('Добро пожаловать!')


for i in range(5):
    a = input('Зайдёте? Да/Нет: ')
    if a == 'Да':
        greeting()
    print('Следующий.\n')
