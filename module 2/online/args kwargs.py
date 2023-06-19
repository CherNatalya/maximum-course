tup = ('14', 20, 'hello')
tup = list(tup)
tup[0] = 14
tup = tuple(tup)
print(tup)
'''def square(i):
    return i ** 2


lst1 = [0 for _ in range(100)]
lst2 = [square(i) for i in range(100)]
lst3 = [i ** 2 if i % 2 == 0 else None for i in range(200)]
# lst = [0 for _ in range(100)] * _ - потому что не использовали переменную (можно заменить и на i)
print(lst2)'''

'''def func(*args, **kwargs):
    print(args)
    print('-------------')
    print(kwargs)


func(15, 'string', lst=[10, 13, 7], call=True)'''

'''a = 10
b = 5
is_bigger = True if a > b else False
print(is_bigger)'''

