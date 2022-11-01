class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(type_data=self.type_data) for j in range(cols)] for i in range(rows)]

    def __check_index(self, index):
        try:
            i, j = index
            a = self.table[i][j]
            return i, j
        except:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        i, j = self.__check_index(item)
        return self.table[i][j].data

    def __setitem__(self, key, value):
        i, j = self.__check_index(key)
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        self.table[i][j].data = value

    def __iter__(self):
        for i in self.table:
            yield (x.data for x in i)

class Cell:
    def __init__(self, data=0, type_data=int):
        self.type_data = type_data
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        else:
            self.__data = data


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"