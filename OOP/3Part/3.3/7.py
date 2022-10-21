import math


class RadiusVector:
    """
    Для описания и работы с n-мерным вектором (у которого n координат). Объекты этого класса должны создаваться командами:
    # создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
    vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0
    # создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
    vector = RadiusVector(1, -5, 3.4, 10)
    """

    def __init__(self, *args):
        if len(args) == 1:
            l = args[0]
            for i in range(l):
                name = 'coord_' + f'{i + 1}'
                self.__dict__[name] = 0
        else:
            for i in range(len(args)):
                name = 'coord_' + f'{i + 1}'
                self.__dict__[name] = args[i]

    def set_coords(self, *args):
        d = list(self.__dict__.keys())
        try:
            for i in range(len(args)):
                self.__dict__[d[i]] = args[i]
        except:
            return

    def get_coords(self):
        return tuple(i for i in self.__dict__.values())

    def __len__(self):
        return len(self.__dict__)

    def __abs__(self):
        values = [pow(i, 2) for i in self.__dict__.values()]
        return math.sqrt(sum(values))


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
res_abs = abs(vector3D)
print(res_abs)
