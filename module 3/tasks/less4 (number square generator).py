myList = (x ** 2 for x in range(0, 1000001))
for i in myList:
    print(i)


def my_lazy_calc(items):
    for item in items:
        yield item ** 2


for it in my_lazy_calc(range(0, 1000001)):
    print(it)
