class Thing:
    id = 1

    def __init__(self, name, price):
        self.id = Thing.id
        Thing.id += 1
        self.name = name
        self.price = price
        self.weight, self.dims, self.memory, self.frm = None, None, None, None

    def get_data(self):
        return tuple(self.__dict__.values())


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())