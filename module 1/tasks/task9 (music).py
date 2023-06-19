violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the night': 6.07,
    'Enjoy the silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'clean': 5.83
}
Sum = 0
num = int(input('Сколько песен выбрать? '))
for i in range(num):
    song = input('Название песни: ')
    Sum += violator_songs.get(song)
print('Общее время звучания:', Sum, 'минуты')
