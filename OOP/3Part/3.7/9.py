# v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторов
# v1 * v2 # умножение соответствующих координат векторов
#
# v1 += 10 # прибавление ко всем координатам вектора числа 10
# v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1
#
# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
# При реализации бинарных операторов +, -, * следует создавать новые
# объекты класса Vector с новыми (вычисленными) координатами.
# При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -,
# * должно генерироваться исключение командой:
# raise ArithmeticError('размерности векторов не совпадают')

import pandas as pd


class Vector:
    def __init__(self, *args):
        self.coords = [*args]

    def make_pd(self, other):
        if isinstance(self, Vector):
            data1 = pd.Series(self.coords)
        else:
            data1 = self
        if isinstance(other, Vector):
            data2 = pd.Series(other.coords)
        else:
            data2 = other
        return data1, data2

    def check_length(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')

    def do(self, other, operation):
        data1, data2 = self.make_pd(other)
        if isinstance(data2, pd.Series):
            self.check_length(other)
            return Vector(*list(getattr(data1, operation)(data2)))
        else:
            self.coords = list(getattr(data1, operation)(other))
            return self

    def __add__(self, other):
        return self.do(other, '__add__')

    def __sub__(self, other):
        return self.do(other, '__sub__')

    def __mul__(self, other):
        return self.do(other, '__mul__')

    def __imul__(self, other):
        return self.do(other, '__add__')

    def __isub__(self, other):
        return self.do(other, '__sub__')

    def __eq__(self, other):
        a, b = self.make_pd(other)
        return all(a == b)

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print()
print()
print()
print()
print(v1 != v2)  # True
print()
print()
print()
print()