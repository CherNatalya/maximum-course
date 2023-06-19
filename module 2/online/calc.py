def calc():
    print("Добро пожаловать")
    print("Поддерживаемые операции: +, -, *, /, **, q")
    try:
        num1 = float(input('Введите число 1: '))
        num2 = float(input('Введите число 2: '))
        sign = input('Действие: ')
    except ValueError:
        return "Недопустимые значения"
    else:
        if sign in ('+', '-', '*', '**', '/', 'q'):
            result = None
            if sign == '+':
                result = num1 + num2
            elif sign == '-':
                result = num1 - num2
            elif sign == '*':
                result = num1 * num2
            elif sign == '**':
                result = num1 ** num2
            elif sign == '/':
                if num2 == 0:
                    result = "Деление на ноль запрещено"
                else:
                    result = num1 / num2
            elif sign == 'q':
                result = 'q'
            return result
        else:
            return 'Неверное действие'


while True:
    res = calc()
    if res == 'q':
        break
    else:
        print(f"Результат: {res}", '-' * 30, sep='\n')
