from random import choice


class Warriors:
    def __init__(self):
        self.health1 = 100
        self.health2 = 100

    def hit(self):
        inp = input()
        if inp:
            attack = choice([1, 2])
            if attack == 1:
                self.health2 -= 20
                print('Атаковал Воин 1', '\n', 'Здоровья у противника: ', self.health2, sep='')
            elif attack == 2:
                self.health1 -= 20
                print('Атаковал Воин 2', '\n', 'Здоровья у противника: ', self.health1, sep='')
            if self.health1 == 0:
                print('Победу одержал Воин 2')
                return
            elif self.health2 == 0:
                print('Победу одержал Воин 1')
                return
        self.hit()


pair = Warriors()
print('Для удара введите любое сообщение')
pair.hit()

