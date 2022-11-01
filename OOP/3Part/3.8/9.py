class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag = []
        self.__current_w = 0

    def __check(self, thing, obj=0):
        if self.__current_w + thing.weight - obj <= self.max_weight:
            return
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __ch_len(self, indx):
        if len(self.bag) > indx >= 0:
            return
        else:
            raise IndexError('неверный индекс')

    def add_thing(self, thing):
        self.__check(thing)
        self.bag.append(thing)
        self.__current_w += thing.weight

    def __getitem__(self, item):
        self.__ch_len(item)
        return self.bag[item]

    def __setitem__(self, key, value):
        self.__check(value, self.bag[key].weight)
        self.__current_w -= self.bag[key].weight
        self.__current_w += value.weight
        self.bag[key] = value

    def __delitem__(self, key):
        del self.bag[key]


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"