def summa_n(num):
    summ = 0
    for n in range(num + 1):
        summ += n
    print('Я знаю, что сумма чисел от 1 до', num, 'равна', summ)


summa_n(int(input()))
