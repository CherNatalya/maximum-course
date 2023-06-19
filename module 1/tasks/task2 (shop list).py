shopping_list = ['bread', 'tomatoes', 'milk', 'ketchup', 'orange juice', 'chocolate bar']
# 1) добавим ещё 1 пункт
shopping_list.append('cucumbers')
# 2) заменим 2 пункт на новый
shopping_list[1] = 'apples'
# 3) выведем длину списка
print(len(shopping_list))
# 4) отсортируем список по алфавиту
shopping_list.sort()
# 5)удалим последний пункт списка
del shopping_list[-1]
