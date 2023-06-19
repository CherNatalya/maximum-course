goods = [
    {
        "name": "Iphone 14",
        "brand": "Apple",
        "price": 1200
    },
    {
        "name": "Samsung Galaxy A53",
        "brand": "Samsung",
        "price": 500
    },
    {
        "name": "Redmi 9",
        "brand": "Xiaomi",
        "price": 400
    }
]

if __name__ == '__main__':
    # здесь должно быть то, что нужно импортировать
    pass
'''print(list(map(lambda x: x['price']*20, sorted(filter(lambda item: item['brand'] == 'Xiaomi', goods), key=lambda item:
                                               item["price"])[:3])))
apple_list = list(filter(lambda item: item['brand'] == "Apple", goods))
print(apple_list)
numbers = ['1', '2', '3', '4', '5']
numbers = list(map(lambda num: int(num) ** 2, numbers))
print(numbers)'''
name_list = ['Данил', 'Никита', 'Настя', 'Катя']
surname_list = ['Иванов', 'Сидоров', 'Горшкова', 'Соловьёва']
'''full_name_list = list(map(lambda name, surname: f"{name} {surname}", name_list, surname_list))
print(full_name_list)'''
'''indexed_goods = []
for ind, item in enumerate(goods):
    indexed_goods.append((ind + 1, item))
print(indexed_goods)'''
patronymic_list = ['Сергеевич', 'Анддреевич', 'Станиславовна']
for name, surname, patronymic in zip(name_list, surname_list, patronymic_list):
    print(name, surname, patronymic)
