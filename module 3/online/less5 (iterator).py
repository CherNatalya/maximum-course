import random
'''import time
from types import TracebackType


class RunningJudge:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb: TracebackType):
        t = time.time() - self.start
        print(f'Время работы кода: {round(t, 2)} сек.')
        if exc_type is TypeError:
            return True


with RunningJudge() as t1:
    my_list = [x for x in range(1, 100000000)]
    my_list += 's'
'''

'''my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i, end=' ')
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))'''


class RandomIter:
    def __init__(self, limit):
        self.counter = limit
        self.__reload = limit

    def __next__(self):
        if self.counter == 0:
            raise StopIteration
        self.counter -= 1
        return random.randint(0, 100)

    def __iter__(self):
        self.counter = self.__reload
        return self


rand_iter = RandomIter(5)
for _ in range(6):
    print(next(rand_iter))

