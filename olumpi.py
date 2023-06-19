num = list(map(int, str(input())))
Sum = 0
for n in range(len(num)):
    if n % 2 == 0:
        Sum += num[n]
    else:
        Sum -= num[n]
print(Sum)
