# coord = v[i] # получение значения i-й координаты (целое число, отсчет с нуля)
# coords_1 = v[start:stop] # получение среза (набора) координат в виде кортежа
# coords_2 = v[start:stop:step] # получение среза (набора) координат в виде кортежа
# v[i] = value # изменение i-й координаты
# v[start:stop] = [val_1, val_2, ...] # изменение сразу нескольких координат
# v[start:stop:step] = [val_1, val_2, ...] # изменение сразу нескольких координат
class RadiusVector:
    def __init__(self, *args):
        self.__coords = [*args]

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, coords):
        self.__coords = coords

    def __getitem__(self, item):
        if isinstance(item, slice):
            return tuple(self.coords[item])
        else:
            return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value



v = RadiusVector(1, 1, 1, 1)
print(v[1])  # 1
v[:] = 1, 2, 3, 4
print(v[2])  # 3
print(v[1:])  # (2, 3, 4)
v[0] = 10.5
