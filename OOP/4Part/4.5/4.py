class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    __uid = 0

    def __new__(cls, *args, **kwargs):
        cls.__uid += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self._name, self._weight, self._price = name, weight, price
        self.__id = self.__uid

    def get_id(self):
        return self.__id
