import random


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = tuple([tuple([Cell() for j in range(3)]) for i in range(3)])
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False
        self.__moves = 3

    @staticmethod
    def __check_index(index):
        if not (3 > index[0] >= 0 and 3 > index[0] >= 0):
            raise IndexError('некорректно указанные индексы')

    def __check_game(self):
        lst = []

        for i in range(3):
            temp_lines = []
            temp_column = []

            # Подсчет значений по строкам
            temp_lines.append(list(map(lambda x: x.value, self.pole[i][:])))

            # Подсчет значений по столбцам
            for j in range(3):
                temp_column.append(self.pole[i][i].value)

            lst.append(sum(*temp_lines))
            lst.append(sum(temp_column))

        temp_diagonal1 = [self.pole[0][0].value, self.pole[1][1].value, self.pole[2][2].value]
        temp_diagonal2 = [self.pole[0][2].value, self.pole[1][1].value, self.pole[2][0].value]
        lst.append(sum([self.pole[0][0].value, self.pole[1][1].value, self.pole[2][2].value]))
        lst.append(sum([self.pole[0][2].value, self.pole[1][1].value, self.pole[2][0].value]))

        self.__moves -= 1

        if not self.__moves:
            # Выбор победителя
            if 3 in lst:
                self.__is_human_win = True
            elif 6 in lst:
                self.__is_computer_win = True
            else:
                self.__is_draw = True

    def __bool__(self):
        return not all((self.__is_human_win, self.__is_computer_win, self.__is_draw))

    def init(self):
        self.__init__()

    def show(self):
        for i in self.pole:
            for j in i:
                if j.value == self.FREE_CELL:
                    print('*', end=' ')
                elif j.value == self.HUMAN_X:
                    print('X', end=' ')
                elif j.value == self.COMPUTER_O:
                    print('0', end=' ')
            print()

    def human_go(self):
        while True:
            try:
                index = tuple(map(int, input('Ваш ход- ').split()))
                self.__check_index(index)
                if self.pole[index[0]][index[1]]:
                    self.pole[index[0]][index[1]].value = self.HUMAN_X
                    break
                else:
                    print('Клетка занята, введите другой индекс')
            except IndexError:
                print('Введите индекс в виде: i j, через пробел, где i и j число от 0 до 2')
        self.__check_game()

    def computer_go(self):
        while True:
            i = random.randrange(0, 3)
            j = random.randrange(0, 3)
            if self.pole[i][j]:
                self.pole[i][j].value = self.COMPUTER_O
                break
            else:
                continue
        self.__check_game()

    def __getitem__(self, item):
        self.__check_index(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        if value not in (0, 1, 2):
            raise ValueError
        self.pole[key[0]][key[1]].value = value
        self.__check_game()

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, is_human_win):
        self.__is_human_win = is_human_win

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, is_computer_win):
        self.__is_computer_win = is_computer_win

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, is_draw):
        self.__is_draw = is_draw


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not self.value


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe,
                                                                                 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[
           0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[
    1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
