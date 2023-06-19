import emoji
'''
animals = ['cat', 'dog', 'pig', 'wolf', 'fox', 'duck', 'bear', 'frog', 'elefant', 'mouse']
print(random.choice(animals))
'''
print(emoji.emojize(':red_heart:'), end='')
print(emoji.emojize(':hedgehog:'))
emojis = []
for i in range(3):
    emojis.append(emoji.emojize(input('Enter :emoji: without extra characters, replacing the emoji with your own:) ')))
print(*emojis, sep='')
