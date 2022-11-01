import re


class StringDigit(str):
    def __init__(self, string):
        self.__check_string(string)


    @staticmethod
    def __check_string(string):
        for i in string:
            if i not in ("0123456789"):
                raise ValueError("в строке должны быть только цифры")
        return string

    def __add__(self, other):
        self.__check_string(other)
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        return StringDigit(other.__add__(self))


sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"

try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"