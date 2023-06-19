'''englishDict = {
    'яблоко': 'apple',
    'молоко': 'milk',
    'кот': 'cat',
    'собака': 'dog'
}
word = input('Введите слово: ')
print(word, 'на английском будет', englishDict.get(word))
'''

films = {
    'начало': 'Леонардо Ди Каприо',
    'пираты карибского моря': 'Джонни Дэпп',
    'миссия невыполнима': 'Том Круз'
}
favActor = 'Джонни Дэпп'
film = input('Введите название фильма: ')
film = film.lower()
actor = films.get(film)
if film in films:
    actor = films.get(film)
    if actor == favActor:
        print('О, я посмотрю этот фильм')
    else:
        print('Не, мне не нравится')
else:
    print('Такого фильма нет в базе')
