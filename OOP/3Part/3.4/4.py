class NewList:
    """
    lst = NewList()  # пустой список
    lst = NewList([-1, 0, 7.56, True])  # список с начальными значениями """

    def __init__(self, lst=None):
        self._lst = lst[:] if lst else []

    def get_list(self):
        """Для возвращения результирующего списка объекта класса NewList"""
        return self._lst

    def __sub__(self, other):
        temp = other if type(other) == list else other.get_list()
        return NewList(self.__subtract(self._lst, temp))

    def __rsub__(self, other):
        return NewList(self.__subtract(other, self._lst))

    @staticmethod
    def __subtract(lst1, lst2):
        if len(lst2) == 0:
            return lst1
        sub = lst2[:]
        return [x for x in lst1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res


# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True]  # NewList: [0, 1, 2, 3, True] - [0, True] = [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_4.lst)
