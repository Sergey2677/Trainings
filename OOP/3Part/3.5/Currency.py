class Money:
    def __init__(self, volume=0.):
        self.cb, self.volume = None, volume

    @property
    def cb(self): return self.__cb

    @cb.setter
    def cb(self, value): self.__cb = value

    @property
    def volume(self): return self.__volume

    @volume.setter
    def volume(self, value): self.__volume = value

    def __abs__(self):
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")
        return self.cb.convert(self.volume, self.prop, 'rub')

    def __eq__(self, other): return abs(abs(self) - abs(other)) <= 0.1

    def __gt__(self, other): return abs(self) - abs(other) > 0.1

    def __ge__(self, other): return abs(self) - abs(other) >= 0.1


class MoneyR(Money): prop = 'rub'


class MoneyD(Money): prop = 'dollar'


class MoneyE(Money): prop = 'euro'


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return None

    @classmethod
    def register(cls, money):
        if isinstance(money, Money):
            money.cb = cls

    @classmethod
    def convert(cls, _value, _from, _to):
        if _from == _to:
            return _value
        return _value * cls.rates.get(_to) / cls.rates.get(_from)
