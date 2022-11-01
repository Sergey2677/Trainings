class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __setattr__(self, key, value):
        value = float(value)
        if value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        else:
            object.__setattr__(self, key, value)


s_inp = input()
lst_dims = sorted([Dimensions(*i.split()) for i in s_inp.split(';')], key=lambda x: hash(x))
