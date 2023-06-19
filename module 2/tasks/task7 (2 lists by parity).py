list1 = []
list2 = []
for n in range(10):
    num = float(input('Введите число: '))
    list1.append(num) if num % 2 != 0 else list2.append(num)
print(list1, list2)
