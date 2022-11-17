class Track:
    def __init__(self, *args):
        self.__points = [*args]

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points = [pt] + self.__points

    def pop_back(self):
        del self.__points[-1]

    def pop_front(self):
        del self.__points[0]


class PointTrack:
    def __init__(self, x, y):
        self._x, self._y = x, y

    def __setattr__(self, key, value):
        if type(value) not in (float, int):
            raise TypeError('координаты должны быть числами')
        object.__setattr__(self, key, value)

    def __str__(self):
        return f"PointTrack: {self._x}, {self._y}"


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
