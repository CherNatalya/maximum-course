import random
animals = []
descriptions = []
for num in range(3):
    name = input()
    animals.append(name)
for num in range(3):
    adj = input()
    descriptions.append(adj)
for num in range(3):
    print(random.choice(animals), random.choice(descriptions))
