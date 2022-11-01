import math


class Value:
    def __set_name__(self, owner, item):
        self.item = "_" + item

    def __get__(self, instance, owner):
        return instance.__dict__[self.item]

    def __set__(self, instance, value):
        if type(value) in (int, float) and value > 0:
            instance.__dict__[self.item] = value
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")


class Triangle:
    a = Value()
    b = Value()
    c = Value()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.__check(a, b, c)

    def __check(self, a, b, c):
        if a < b + c and b < a + c and c < a + b:
            return True
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        """s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника"""
        p = len(self) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
