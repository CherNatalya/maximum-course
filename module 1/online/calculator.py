num1 = float(input('Введите число 1: '))
num2 = float(input('Введите число 2: '))
sign = input('Что нужно сделать: ')
if sign == '+':
    print('Сумма равна', num1 + num2)
elif sign == '-':
    print('Разность равна', num1 - num2)
elif sign == '*':
    print('Произведение равно', num1 * num2)
elif sign == '/':
    print('Частное равно', num1 / num2)
else:
    print('Неверное действие')
