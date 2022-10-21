class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a=0, b=0, c=0):
        self.__a = a
        self.__b = b
        self.__c = c

    @classmethod
    def check(cls, item):
        return cls.MAX_DIMENSION >= item >= cls.MIN_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def volume(self):
        return self.__a * self.__b * self.__c

    def __setattr__(self, key, value):
        if self.check(value):
            object.__setattr__(self, key, value)

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __le__(self, other):
        return self.volume() <= other.volume()


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim

trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())