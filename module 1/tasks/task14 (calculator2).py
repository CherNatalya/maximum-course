def calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2


file = open('result.txt', 'w')
file.write(str(calculator(int(input()), int(input()), input())))
