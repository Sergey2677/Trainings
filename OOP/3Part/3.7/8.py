import random


class GamePole:
    flag = True
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.flag:
            cls.flag = False
            cls.obj = super().__new__(cls)
            return cls.obj
        return cls.obj

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for j in range(self.M)] for i in range(self.N)]

    @property
    def pole(self):
        return self.__pole_cells

    # Инициализирует поле в начале игры
    def init_pole(self):
        """Для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми)"""
        mines = self.total_mines
        while mines:
            i = random.randint(0, self.N - 1)
            j = random.randint(0, self.M - 1)
            if not self.pole[i][j].is_mine:
                self.pole[i][j].is_mine = True
                mines -= 1
        self.close()
        self.search_mine()

    # Закрывает все клетки
    def close(self):
        for i in self.pole:
            for j in i:
                if j.is_open:
                    j.is_open = False

    # Ищет клетки в которых присутствует мина
    def search_mine(self):
        for i, e in enumerate(self.__pole_cells):
            for i1, e1 in enumerate(e):
                if e1.is_mine:
                    self.count_mines_around_cell(i, i1)

    # Увеличивает счетчик у каждой соседней клетки от мины
    def count_mines_around_cell(self, i, j):
        coords = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        p = self.__pole_cells
        for i1, j1 in coords:
            ii = i + i1
            jj = j + j1
            if ii < 0 or ii >= self.N or jj < 0 or jj >= self.M:
                continue
            else:
                if not p[ii][jj].is_mine:
                    p[ii][jj].number += 1

    # Открывает клетку
    def open_cell(self, i, j):
        """Открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля;
        метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True"""
        try:
            self.pole[i][j].is_open = True
        except:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    # Выводит поле в консоль
    def show_pole(self):
        """Отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание)"""
        for i in self.__pole_cells:
            for j in i:
                if not j:
                    if j.is_mine:
                        print('*', end=' ')
                    else:
                        print(j.number, end=' ')
                else:
                    print("#", end=' ')
            print()


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        if type(is_mine) is bool:
            self.__is_mine = is_mine
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if type(number) is int and 8 >= number >= 0:
            self.__number = number
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        if type(is_open) is bool:
            self.__is_open = is_open
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not self.is_open


def test_game():
    p1 = GamePole(10, 20, 10)
    p2 = GamePole(10, 20, 10)
    assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
    p = p1

    cell = Cell()
    assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
        Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

    cell.is_mine = True
    cell.number = 5
    cell.is_open = True
    assert bool(cell) == False, "функция bool() вернула неверное значение"

    try:
        cell.is_mine = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        cell.number = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    p.init_pole()
    m = 0
    for row in p.pole:
        for x in row:
            assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
            if x.is_mine:
                m += 1

    assert m == 10, "на поле расставлено неверное количество мин"
    p.open_cell(0, 1)
    p.open_cell(9, 19)

    try:
        p.open_cell(10, 20)
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    def count_mines(pole, i, j):
        n = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                ii, jj = k + i, l + j
                if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                    continue
                if pole[ii][jj].is_mine:
                    n += 1

        return n

    for i, row in enumerate(p.pole):
        for j, x in enumerate(row):
            if not p.pole[i][j].is_mine:
                m = count_mines(p.pole, i, j)
                assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
