import random


class RandomIter:
    def __next__(self):
        return random.randint(0, 100)

    def __iter__(self):
        return self


rand_iter = RandomIter()
for _ in rand_iter:
    print(next(rand_iter))
