class User:
    def __init__(self, name, damage):
        self.health = 100
        self.name = name
        self.damage = damage

    def health_down(self, damage):
        self.health -= damage
        print(f"Здоровье {self.name}: {self.health}")

    def attack(self, enemy):
        if enemy.health <= 0:
            print(f"{enemy.name} уничтожен")
        else:
            print(f"{self.name} атаковал игрока {enemy.name}")
        enemy.health_down(self.damage)


class Magic(User):
    def __init__(self, name, damage, heal):
        super().__init__(name, damage)
        self.health = 100
        self.heal = heal


class Warrior(User):
    def __init__(self, name, damage, protect):
        super().__init__(name, damage)
        self.health = 100 + protect


class Archer(User):
    def __init__(self, name, damage):
        super().__init__(name, damage)
        self.health = 100
        self.damage = damage * 1.5


user1 = User('Player1', 40)
user2 = User('Player2', 25)
user2.attack(user1)
us1 = Magic('Mag', 30, 30)
us2 = Warrior('War', 45, 50)
us3 = Archer('Arch', 30)
print(us1.name, us1.damage, us1.health, us1.heal)
print(us2.name, us2.damage, us2.health)
print(us3.name, us3.damage, us3.health)