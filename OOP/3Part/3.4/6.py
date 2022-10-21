# Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):
# # добавление нового объекта класса StackObj в конец односвязного списка st
# st = st + obj
# st += obj
# # добавление нескольких объектов в конец односвязного списка
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']
# В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными,
# взятыми из списка (каждый элемент списка для очередного добавляемого объекта).

class Stack:
    """
    Для управления односвязным списком в целом
    Объекты класса Stack создаются командой:
    st = Stack()
    и каждый из них должен содержать локальный атрибут:
    top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).
    Также в классе Stack следует объявить следующие методы:
    push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
    pop_back(self) - удаление последнего объекта из односвязного списка."""

    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            temp = self.top
            while temp.next:
                temp = temp.next
            temp.next = obj

    def pop_back(self):
        if self.top.next is None:
            self.top = None
        else:
            temp = self.top
            prev = None
            while temp.next:
                prev = temp
                temp = temp.next
            temp = prev

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        if type(other) == list:
            objects = []
            for i in other:
                objects.append(StackObj(i))
            for i in objects:
                self.push_back(i)
        else:
            other = StackObj(other)
            self.push_back(other)
        return self


class StackObj:
    """
    Для представления отдельных объектов в односвязным списком
    Объекты класса StackObj должны создаваться командой: obj = StackObj(data)
    где data - строка с некоторыми данными.
    Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
    __data - ссылка на строку с переданными данными;
    __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None)."""

    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
