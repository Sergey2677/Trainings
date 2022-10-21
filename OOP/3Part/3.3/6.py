import math

class Complex:
    """
    Для представления и работы с комплексными числами
    Объекты этого класса должны создаваться командой: cm = Complex(real, img), где
    real - действительная часть комплексного числа (целое или вещественное значение)
    img - мнимая часть комплексного числа (целое или вещественное значение).
    """
    
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, real):
        self.__real = real

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        self.__img = img



    def __setattr__(self, key, value):
        if type(value) in (int, float):
            object.__setattr__(self, key, value)
        else:
            raise ValueError("Неверный тип данных.")


    def __abs__(self):
        return math.sqrt((pow(self.real, 2) + pow(self.img, 2)))


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)