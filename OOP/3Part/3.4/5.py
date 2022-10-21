# lst = lst + 76 # сложение каждого числа списка с определенным числом
# lst = 6.5 + lst # сложение каждого числа списка с определенным числом
# lst += 76.7  # сложение каждого числа списка с определенным числом
# lst = lst - 76 # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst # деление числа на каждый элемент списка
# lst /= 13.0


# class ListMath:
#     def __init__(self, lst=None):
#         self.lst_math = lst[:] if lst and type(lst) == list else []
#
#     def __setattr__(self, key, value):
#         if type(value) == list:
#             if value:
#                 vl = []
#                 for i in value:
#                     if type(i) in (int, float):
#                        vl.append(i)
#                 self.__dict__[key] = vl
#             else:
#                 object.__setattr__(self, key, value)
#         else:
#             object.__setattr__(self, key, value)
#
#     @staticmethod
#     def operation(el, el1, operation):
#         """An operation is a variable that can take values from range 0-3
#         where each value is compared to an operation such as addition or subtraction, division etc."""
#         if type(el) == list:
#             if operation == 0:
#                 return [i + el1 for i in el]
#             elif operation == 1:
#                 return [i - el1 for i in el]
#             elif operation == 2:
#                 return [i * el1 for i in el]
#             elif operation == 3:
#                 return [i / el1 for i in el]
#         else:
#             if operation == 0:
#                 return [el + i for i in el1]
#             elif operation == 1:
#                 return [el - i for i in el1]
#             elif operation == 2:
#                 return [el * i for i in el1]
#             elif operation == 3:
#                 return [el / i for i in el1]
#
#
#     def __add__(self, other):
#         """an operation is 0"""
#         return ListMath(self.operation(self.lst_math, other, 0))
#
#     def __radd__(self, other):
#         """an operation is 0"""
#         return ListMath(self.operation(other, self.lst_math, 0))
#
#     def __sub__(self, other):
#         """an operation is 1"""
#         return ListMath(self.operation(self.lst_math, other, 1))
#
#     def __rsub__(self, other):
#         """an operation is 1"""
#         return ListMath(self.operation(other, self.lst_math, 1))
#
#     def __mul__(self, other):
#         """an operation is 2"""
#         return ListMath(self.operation(self.lst_math, other, 2))
#
#     def __rmul__(self, other):
#         """an operation is 2"""
#         return ListMath(self.operation(other, self.lst_math, 2))
#
#     def __truediv__(self, other):
#         """an operation is 3"""
#         return ListMath(self.operation(self.lst_math, other, 3))
#
#     def __rtruediv__(self, other):
#         """an operation is 3"""
#         return ListMath(self.operation(other, self.lst_math, 3))

class ListMath:
    def __init__(self, arg=[]):
        self.lst_math = [i for i in arg if type(i) in (int, float)]

    def do(self, fn_name, other, new=True):
        result = [getattr(i, fn_name)(other) for i in self.lst_math]
        if new:
            return ListMath(result)
        else:
            self.lst_math = result
            return self

    def __add__(self, other):
        return self.do('__add__', other)

    def __sub__(self, other):
        return self.do('__sub__', other)

    def __rsub__(self, other):
        return self.do('__rsub__', other)

    def __mul__(self, other):
        return self.do('__mul__', other)

    def __rmul__(self, other):
        return self.do('__rmul__', other)

    def __truediv__(self, other):
        return self.do('__truediv__', other)

    def __iadd__(self, other):
        return self.do('__add__', other, False)

    def __isub__(self, other):
        return self.do('__sub__', other, False)

    def __imul__(self, other):
        return self.do('__mul__', other, False)

    def __idiv__(self, other):
        return self.do('__truediv__', other, False)

lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0