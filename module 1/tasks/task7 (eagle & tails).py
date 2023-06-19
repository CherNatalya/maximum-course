import random
user_choice = input('Орёл или решка? ').lower()
random_choice = random.choice(['орёл', 'решка'])
if user_choice == random_choice:
    print('Ты победил')
else:
    print('Ты проиграл')
