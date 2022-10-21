class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self._step = step
        self._size = size

    def __call__(self, matrix):
        # a new list for the largest value in the window size range
        new_lst = []
        # check the matrix size and type of values
        size = len(matrix[0])
        for i in matrix:
            if len(i) != size:
                raise ValueError("Неверный формат для первого параметра matrix.")
            for j in i:
                if not isinstance(j, (int, float)):
                    raise ValueError("Неверный формат для первого параметра matrix.")
        # Going through the values within the window and selecting the maximum one
        for i in range(0, len(matrix), self._step[0]):
            temp = []
            for j in range(0, len(matrix[i]), self._step[1]):
                try:
                    a = matrix[i][j:j + self._size[0]] + matrix[i + 1][j:j + self._size[1]]
                    if len(a) == self._size[0] * self._size[1]:
                        temp.append(max(a))
                except:
                    pass
            try:
                if temp:
                    new_lst.append(temp)
            except:
                pass
        return new_lst


mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
