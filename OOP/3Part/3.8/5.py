class IntegerValue:
    def __set_name__(self, owner, item):
        self.item = "_" + item

    def __get__(self, instance, owner):
        return instance.__dict__[self.item]

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.item] = value


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=CellInteger):
        self.rows = rows
        self.cols = cols
        if not cell:
            raise ValueError('параметр cell не указан')
        self.cells = tuple([tuple([cell() for i in range(cols)]) for j in range(rows)])

    def __check(self, i, j):
        if type(i) == int and self.rows > i >= 0:
            if type(j) == int and self.cols > j >= 0:
                return
        raise IndexError('Индекс не существует')

    def __getitem__(self, item):
        i, j = item
        self.__check(i, j)
        return self.cells[i][j].value

    def __setitem__(self, key, value):
        i, j = key
        self.__check(i, j)
        self.cells[i][j].value = value

tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"