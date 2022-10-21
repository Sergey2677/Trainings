# С объектами класса Box3D должны выполняться следующие операторы:
#
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
#
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
# При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных атрибутов.

class Box3D:
    """
    box = Box3D(width, height, depth)
    где:
    width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)"""
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_res(self, key, value, operation):
        r = getattr(getattr(self, key), operation)(value)
        return r if r != NotImplemented else getattr(value, '__r' + operation[2:])(getattr(self, key))

    def do(self, operation, obj2):
        if isinstance(obj2, Box3D):
            res = [self.get_res(key, value, operation) for key, value in obj2.__dict__.items()]
        else:
            res = [self.get_res(key, obj2, operation) for key, value in self.__dict__.items()]
        return Box3D(*res)

    def __add__(self, other):
        return self.do('__add__', other)

    def __radd__(self, other):
        return self.do('__add__', other)

    def __sub__(self, other):
        return self.do('__sub__', other)

    def __rsub__(self, other):
        return self.do('__rsub__', other)

    def __mul__(self, other):
        return self.do('__mul__', other)

    def __rmul__(self, other):
        return self.do('__mul__', other)

    def __mod__(self, other):
        return self.do('__mod__', other)

    def __floordiv__(self, other):
        return self.do('__floordiv__', other)
