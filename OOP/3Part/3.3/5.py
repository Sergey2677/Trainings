class LinkedList:
    """
    Объявите класс LinkedList (связный список)
    Здесь создается список из связанных между собой объектов класса ObjList
    Объекты класса LinkedList должны создаваться командой: linked_lst = LinkedList(),
    и содержать локальные атрибуты:
    head - ссылка на первый объект связного списка (если список пуст, то head = None);
    tail - ссылка на последний объект связного списка (если список пуст, то tail = None).
    Также с объектами класса LinkedList должны поддерживаться следующие операции:
    len(linked_lst) - возвращает число объектов в связном списке;
    linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        """
        Добавление нового объекта obj класса ObjList в конец связного списка
        """
        if self.tail:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj
        elif self.tail is None and self.head:
            obj.prev = self.head
            self.head.next = obj
            self.tail = obj
        if self.head is None:
            self.head = obj

    def remove_obj(self, indx):
        """
        Удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля
        """
        if indx == 0:
            self.head = None
            self.tail = None
            return
        temp = self.head
        counter = 0
        while counter < indx:
            temp = temp.next
            counter += 1
        if temp == self.tail:
            if temp.prev:
                if temp.prev == self.head:
                    self.tail = self.head
                    self.head.next = None
                    return
                temp.prev.next = None
                self.tail = temp.prev
            elif temp.prev == self.head:
                self.head.next = None
        else:
            temp.prev.next = temp.next

    def __len__(self):
        temp = self.head
        if temp:
            counter = 0
            while temp:
                counter += 1
                temp = temp.next
            return counter
        else:
            return 0

    def __call__(self, indx):
        if self.head:
            start = 0
            n = self.head
            while start != indx:
                n = n.next
                if not n:
                    raise IndexError('LinkedList index out of range')
                start += 1
            return n.data


class ObjList:
    """
    Объекты этого класса создаются командой: obj = ObjList(data),
    """

    def __init__(self, data):
        """
        __data - ссылка на строку с данными
        __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None)
        __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None)
        """

        self.__next = None
        self.__data = data
        self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev
        
    


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
# ln.remove_obj(2)
# ln.remove_obj(1)
# ln.remove_obj(0)
# assert ln.head is None and ln.tail is None
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"