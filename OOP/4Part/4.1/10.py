class Vector:
    def __init__(self, *args):
        self.coords = [*args]

    def __calculate(self, other, operation):
        if isinstance(other, (Vector, VectorInt)):
            if len(self.coords) != len(other.coords):
                raise TypeError('размерности векторов не совпадают')
            res = [getattr(self.coords[i], operation)(other.coords[i]) for i in range(len(self.coords))]
        else:
            res = [getattr(self.coords[i], operation)(other) for i in range(len(self.coords))]
        types_value = all(i for i in map(lambda x: type(x) == int, res))
        if types_value:
            return VectorInt(*res)
        else:
            return Vector(*res)

    def get_coords(self):
        return tuple(self.coords)

    def __add__(self, other):
        return self.__calculate(other, '__add__')

    def __sub__(self, other):
        return self.__calculate(other, '__sub__')


class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__(*args)

    def __setattr__(self, key, value):
        types = all(i for i in map(lambda x: type(x) == int, value))
        if not types:
            raise ValueError('координаты должны быть целыми числами')
        else:
            object.__setattr__(self, key, value)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v3 = v1 + v2

assert (v1 + v2).get_coords() == (
4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"