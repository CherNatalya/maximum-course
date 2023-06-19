goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678'
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42}
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520}
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150}
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97}
    ]
}
price = 0
Sum = 0
good = input('Введите товар: ')
code = goods.get(good)
for b in store.get(code):
    Sum += b.get('quantity')
    price += b.get('quantity') * b.get('price')
print(good, '-', Sum, 'шт.,', 'стоимость', price, 'руб.')
