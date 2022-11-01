class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, game):
        if not self.__dict__.get('name', False):
            self.name = game


class Game(Singleton):
    ...


g = Game('asdads')

g1 = Game('asd')


print(g.__dict__)
print(g1.__dict__)