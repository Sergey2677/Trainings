# Minesweeper
import random

class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=True):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = []

    def init(self):
        # Initialization a mines surface
        self.pole = [[Cell() for i in range(self.N)] for i in range(self.N)]

        # Set mines
        mines = 0
        while mines != self.M:
            x = random.randrange(self.N)
            y = random.randrange(self.N)
            if self.pole[x][y].mine == False:
                self.pole[x][y] = Cell(mine=True)
                mines += 1

        # Check mines
        index = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    mines = sum((self.pole[i + a][j + b].mine for a, b in index if
                                 0 <= i + a <= self.N - 1 and 0 <= j + b <= self.N - 1))
                    self.pole[i][j].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.init()
pole_game.show()
