import contextlib
'''import time
my_range = range(1, 10)
print(my_range)
print(list(my_range))
print('Сейчас создается строгий список')'''
'''my_range1 = [time.sleep(1) for x in range(3)]
print('Строгий список закончил создаваться')
print('Создается ленивый список')
my_range2 = (time.sleep(1) for x in range(3))
print('Ленивый список создался')
for i in my_range2:
    pass
print('Программа завершена')'''


'''def my_lazy_calc(items):
    for item in items:
        yield item


for it in my_lazy_calc([1, 2, 3, 4]):
    print(it)'''

'''my_file = open("test.txt", 'w')
my_file.write("Привет, мир")
my_file.close()

with open('test.txt', 'w') as f:
    f.write('Hello world')
    print(f.closed)

print(f.closed)'''


'''@contextlib.contextmanager
def str_reverse(my_str):
    print("Входим в контекстный менеджер")
    yield my_str[::-1]
    print("Выходим из км")


with str_reverse('Hello world') as reverse:
    print(f"Выполняется код: {reverse}")'''


@contextlib.contextmanager
def exc_handler(exc):
    try:
        yield
    except exc:
        print("Произошло исключение")


with exc_handler(ZeroDivisionError):
    list1 = [1, 2]
    print(7 / 0)
