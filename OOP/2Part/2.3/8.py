class SuperShop:
    def __init__(self, name, goods=[]):
        self.name = name
        self.goods = goods

    def add_product(self, product):
        """Добавление товара в магазин (в конец списка goods)"""
        self.goods.append(product)

    def remove_product(self, product):
        """Удаление товара из магазина (из списка goods)"""
        self.goods.remove(product)


class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, item):
        self.item = "_" + item

    def __get__(self, instance, owner):
        return instance.__dict__[self.item]

    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) <= self.max_length:
            instance.__dict__[self.item] = value


class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def __set_name__(self, owner, item):
        self.item = "_" + item

    def __get__(self, instance, owner):
        return instance.__dict__[self.item]

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            instance.__dict__[self.item] = value


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")


