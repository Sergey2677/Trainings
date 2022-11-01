class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.arr = [cell() for i in range(self.max_length)]

    def __check(self, indx):
        if type(indx) == int and len(self.arr) > indx >= 0:
            return
        else:
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item):
        self.__check(item)
        return self.arr[item].value

    def __setitem__(self, key, value):
        self.__check(key)
        self.arr[key].value = value

    def __str__(self):
        a = [str(i.value) for i in self.arr]
        return ' '.join(a)


class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) == int:
            self.__value = value
        else:
            raise ValueError('должно быть целое число')


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5  # должно генерироваться исключение ValueError
ar_int[10] = 1  # должно генерироваться исключение IndexError
