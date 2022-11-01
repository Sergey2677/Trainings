class ItemAttrs:
    def __init__(self):
        self.keys = list(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[self.keys[item]]

    def __setitem__(self, key, value):
        self.__dict__[self.keys[key]] = value


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
