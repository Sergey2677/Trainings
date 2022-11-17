from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        ...

    @abstractmethod
    def pop_back(self):
        ...


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if not self._top:
            self._top = obj
        else:
            temp = self._top
            while temp._next:
                temp = temp._next
            temp._next = obj

    def pop_back(self):
        if self._top:
            temp_prev = self._top
            temp_next = temp_prev._next
            if not temp_next:
                obj = self._top
                self._top = None
                return obj
            while temp_next._next:
                temp_prev = temp_next
                temp_next = temp_next._next

            temp_prev._next = None
            return temp_next


class StackObj:
    def __init__(self, data):
        self._data, self._next = data, None


assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()  # type: ignore
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"

st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"
