class StackObj:
    def __init__(self, data):
        self.__data = None
        self.__next = None
        self.data = data

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
        if isinstance(next, StackObj) or next is None:
            self.__next = next

class Stack:

    def __init__(self):
        self.top = None

    def push(self, obj):
        """Добавление объекта класса StackObj в конец односвязного списка"""
        temp = self.top
        if self.top is None:
            self.top = obj
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = obj

    def pop(self):
        """Извлечение последнего объекта с его удалением из односвязного списка"""
        if self.top is None:
            return
        last_item = self.top
        temp1 = self.top
        while last_item.next is not None:
            last_item =  last_item.next
        if last_item == temp1:
            self.top = None
            return last_item
        while temp1.next != last_item:
            temp1 = temp1.next
        temp1.next = None
        return last_item

    def get_data(self):
        """Получение списка из объектов односвязного списка
        (список из строк локального атрибута __data каждого объекта в порядке их добавления,
        или пустой список, если объектов нет)"""
        s = []
        n = self.top
        if n is None:
            return s
        while n.next is not None:
            s.append(n.data)
            n = n.next
        s.append(n.data)
        return s

st = Stack()
st.push(StackObj("obj1"))
print(st.get_data())
print(st.pop())
print(st.get_data())
