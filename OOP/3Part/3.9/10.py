class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            self.rows, self.cols, self.fill_value = args[0], args[1], args[2]
            self.list2D = [[self.fill_value for j in range(self.cols)] for i in range(self.rows)]
        else:
            self.list2D = args[0]

    def __do(self, other, operation):
        if isinstance(other, Matrix):
            if len(self.list2D) == len(other.list2D) and len(self.list2D[0]) == len(other.list2D[0]):
                l_row = len(self.list2D)
                l_column = len(self.list2D[0])
                lst = [[getattr(self.list2D[i][j], operation)(other.list2D[i][j]) for j in range(l_column)] for i in
                       range(l_row)]
            else:
                raise ValueError('операции возможны только с матрицами равных размеров')
        else:
            lst = [[getattr(self.list2D[i][j], operation)(other) for j in range(len(self.list2D[0]))] for i in
                   range(len(self.list2D))]
        return Matrix(lst)

    def __check_index(self, item):
        i, j = item
        if type(i) != int or type(j) != int or not (len(self.list2D) > i >= 0 and len(self.list2D[0]) > j >= 0):
            raise IndexError

    def __setattr__(self, key, value):
        if key in ('rows', 'cols') and type(value) != int:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        elif key == 'fill_value' and type(value) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
        elif key == 'list2D' and type(value) is list:
            check = all(map(lambda x: len(x) == len(value[0]), value))
            check_value = all(map(lambda x: type(x) in (int, float), (j for i in value for j in i)))
            if not check or not check_value:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        object.__setattr__(self, key, value)

    def __getitem__(self, item):
        self.__check_index(item)
        i, j = item
        return self.list2D[i][j]

    def __setitem__(self, key, value):
        self.__check_index(key)
        i, j = key
        if type(value) in (int, float):
            self.list2D[i][j] = value
        else:
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __add__(self, other):
        return self.__do(other, '__add__')

    def __iadd__(self, other):
        self.__add__(other)

    def __sub__(self, other):
        return self.__do(other, '__sub__')

    def __isub__(self, other):
        self.__sub__(other)


list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2, 7], [3, 4, 6]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2, 5], [3, 4, 5]])
m2 = Matrix([[1, 1, 7], [1, 1, 7]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
