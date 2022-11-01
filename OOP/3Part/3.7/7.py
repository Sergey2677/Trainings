class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return len(self.__dict__.keys()) == 4

    def get_coords(self):
        try:
            return (self.x1, self.y1, self.x2, self.y2)
        except:
            raise AttributeError('нет координат для извлечения')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for i in lst_geom:
    if i:
        i.get_coords()