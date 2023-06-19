import random
print('Компьютер загадал число от 1 до 10. Попробуй угадать :)')
number = random.randint(1, 100)
wrong = 0
for i in range(7):
    myNumber = int(input('Вводи число: '))
    if myNumber == number:
        print('Ого, ты угадал :)')
        break
    elif myNumber > number:
        print('Не угадал, число меньше')
        wrong += 1
    elif myNumber < number:
        print('Не угадал, число больше')
        wrong += 1
if wrong == 7:
    print('Ты проиграл, вот правильное число:', number)
