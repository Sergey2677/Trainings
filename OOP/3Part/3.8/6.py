# Дополнительно в классе Stack нужно объявить магические методы для
# обращения к объекту стека по его индексу, например:
# obj_top = st[0] # получение первого объекта
# obj = st[4] # получение 5-го объекта стека
# st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый


class Stack:
    def __init__(self):
        self.top = None
        self.__length = 0

    def push(self, obj):
        if self.top:
            self[self.__length - 1].next = obj
        else:
            self.top = obj
        self.__length += 1

    def pop(self):
        if self.__length > 1:
            deleted = self[self.__length - 1]
            self[self.__length - 2].next = None
        else:
            deleted = self.top
            self.top = None
        self.__length -= 1
        return deleted

    def __check(self, indx):
        if type(indx) and 0 <= indx < self.__length:
            return
        else:
            raise IndexError

    def __getitem__(self, item):
        self.__check(item)
        temp = self.top
        if not temp:
            raise IndexError
        while item:
            temp = temp.next
            item -= 1
        return temp

    def __setitem__(self, key, value):
        self.__check(key)
        if key:
            value.next = self[key + 1]
            self[key - 1].next = value
        else:
            value.next = self.top[key + 1]
            self.top = value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
