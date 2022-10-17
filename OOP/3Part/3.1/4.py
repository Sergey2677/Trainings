class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)

class Product:
    uid = 0

    def __new__(cls, *args, **kwargs):
        cls.uid += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.id = self.uid
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        d = {'id': type(value) is int, 'name': type(value) is str, 'weight': type(value) in (int, float), 'price': type(value) in (int, float)}
        if d[key]:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
