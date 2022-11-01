# Для объектов класса Body должны быть реализованы операторы сравнения:
# Масса тела вычисляется по формуле: m = ro * volume
# body1 > body2  # True, если масса тела body1 больше массы тела body2
# body1 == body2 # True, если масса тела body1 равна массе тела body2
# body1 < 10     # True, если масса тела body1 меньше 10
# body2 == 5     # True, если масса тела body2 равна 5

class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def convert(self):
        return self.ro * self.volume

    def __eq__(self, other):
        if isinstance(other, Body):
            return self.convert() == other.convert()
        else:
            return self.convert() == other

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.convert() < other.convert()
        else:
            return self.convert() < other