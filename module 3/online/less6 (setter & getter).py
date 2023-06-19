class Year:
    def __init__(self, num: int, season: str):
        self.__num = num
        self.__season = season
        self.__leap = False
        if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
            self.__leap = True

    @property
    def num(self) -> int:
        return self.__num

    @property
    def season(self) -> str:
        return self.__season

    @property
    def leap(self) -> str:
        return "Год високосный" if self.__leap else "Год не високосный"

    @season.setter
    def season(self, season: str):
        if season in ("зима", "весна", "лето", "осень"):
            self.__season = season
        else:
            raise Exception("Недопустимое значение")


year = Year(2020, 'зима')
year.season = 'лето'
print(year.num, year.season, year.leap)
try:
    year.season = 'Ядерную зиму'
except Exception as e:
    print(f"Ошибка: {e}")


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > self.__age:
            self.__age = age
        else:
            print('Человек может только стареть')

    @name.deleter
    def name(self):
        del self.__name

    @age.deleter
    def age(self):
        del self.__age


person = Person('Наталья', 16)
del person.name
