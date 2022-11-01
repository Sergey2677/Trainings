class TicTacToe:
    def __init__(self):
        self.pole = tuple([tuple([Cell() for j in range(3)]) for i in range(3)])
        self.clear()

    def clear(self):
        for i in self.pole:
            for j in i:
                j.is_free = False
                j.value = 0


    def __get_item(self, i, j):
        res = []
        if isinstance(i, slice):
            for x in range(len(self.pole)):
                res.append(self.pole[x][j])
        else:
            res = self.pole[i][j]
        return res


    def __getitem__(self, item):
        try:
            temp = self.__get_item(item[0], item[1])
            if isinstance(temp, Cell):
                return temp.value
            else:
                res = []
                for i in temp:
                    res.append(i.value)
                return tuple(res)
        except:
            raise IndexError('неверный индекс клетки')

    def __setitem__(self, key, value):
        if not self.__get_item(key[0], key[1]):
            self.__get_item(key[0], key[1]).value = value
        else:
            raise ValueError('клетка уже занята')


class Cell:
    def __init__(self):
        self.is_free = False
        self.value = 0

    def __bool__(self):
        return self.is_free


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"
