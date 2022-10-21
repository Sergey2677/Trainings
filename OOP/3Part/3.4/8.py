# s = it1 + it2 # сумма для двух статей расходов
# s = it1 + it2 + ... + itN # сумма N статей расходов
# При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих объектов класса Item.

class Budget:
    """
    А сам класс Budget должен иметь следующие методы:
    add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
    remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
    get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).
    """
    def __init__(self):
        self.budget = []

    def add_item(self, it):
        self.budget.append(it)

    def remove_item(self, indx):
        self.budget.pop(indx)

    def get_items(self):
        return self.budget



class Item:
    """
    it = Item(name, money)
    где:
    name - название статьи расхода;
    money - сумма расходов (вещественное или целое число)."""
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        else:
            return self.money + other

    def __radd__(self, other):
        return self.__add__(other)

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
    print(s)