class FloatValue:
    def __set_name__(self, owner, item):
        self.item = "_" + item

    def __get__(self, instance, owner):
        return instance.__dict__[self.item]

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        instance.__dict__[self.item] = value

class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value

class TableSheet:
    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.cells = [[Cell() for i in range(self.M)] for j in range(self.N)]

# Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

table = TableSheet(5, 3)
start = 1.0
for i in table.cells:
    for j in i:
        j.value = start
        start += 1

for i in table.cells:
    for j in i:
        print(dir(j))
        print(j.value)
