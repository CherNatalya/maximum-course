class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        elif isinstance(other, float) or isinstance(other, int):
            return self.price + other

    def __sub__(self, other):
        if isinstance(other, Item):
            return self.price - other.price
        elif isinstance(other, float) or isinstance(other, int):
            return self.price - other

    def __mul__(self, other):
        if isinstance(other, Item):
            return self.price * other.price
        elif isinstance(other, float) or isinstance(other, int):
            return self.price * other

    def __floordiv__(self, other):
        if isinstance(other, Item):
            return self.price // other.price
        elif isinstance(other, float) or isinstance(other, int):
            return self.price // other


item1 = Item('Видеокарта GEFORCE 9999 ULTRA', 15_000, 0.8)
item2 = Item('Процессор Intel i20', 12_000, 0.3)
print(item1 + 2.2, item1 + 2, item1 + item2)
print(item1 - 2.2, item1 - 2, item1 - item2)
print(item1 * 2.2, item1 * 2, item1 * item2)
print(item1 // 2.2, item1 // 2, item1 // item2)
