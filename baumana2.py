num = int(input())
Sum = 0
for n in range(num):
    number = input()
    for a in range(len(number)):
        if number[a] == '0':
            Sum += 0 * (16 ** (len(number) - a))
        elif number[a] == '1':
            Sum += 1 * (16 ** (len(number) - a))
        elif number[a] == '2':
            Sum += 2 * (16 ** (len(number) - a))
        elif number[a] == '3':
            Sum += 3 * (16 ** (len(number) - a))
        elif number[a] == '4':
            Sum += 4 * (16 ** (len(number) - a))
        elif number[a] == '5':
            Sum += 5 * (16 ** (len(number) - a))
        elif number[a] == '6':
            Sum += 6 * (16 ** (len(number) - a))
        elif number[a] == '7':
            Sum += 7 * (16 ** (len(number) - a))
        elif number[a] == '8':
            Sum += 8 * (16 ** (len(number) - a))
        elif number[a] == '9':
            Sum += 9 * (16 ** (len(number) - a))
        elif number[a] == 'A':
            Sum += 10 * (16 ** (len(number) - a))
        elif number[a] == 'B':
            Sum += 11 * (16 ** (len(number) - a))
        elif number[a] == 'C':
            Sum += 12 * (16 ** (len(number) - a))
        elif number[a] == 'D':
            Sum += 13 * (16 ** (len(number) - a))
        elif number[a] == 'E':
            Sum += 14 * (16 ** (len(number) - a))
        elif number[a] == 'F':
            Sum += 15 * (16 ** (len(number) - a))