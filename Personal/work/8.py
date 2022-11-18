# 8. Из задачи 7 доработайте списки так, чтобы в каждом из двух списков были
# элементы из другого. Переведите списки в множества. Возьмите объединение и
# пересечение.

class CustomID:
    def __init__(self, lst):
        self.__lst = lst

    def __hash__(self):
        return hash((self.__lst[1], self.__lst[2]))


class CustomID2:
    def __init__(self, lst):
        self.__lst = lst

    def __hash__(self):
        return hash((self.__lst[1]))

lst_in = [['Товар1', 1, 500], ['Товар2', 7, 1000], ['Товар1', 6, 900]]

set1 = set([id(hash(CustomID(i))) for i in lst_in])
set2 = set([id(hash(CustomID2(i))) for i in lst_in])

print(set1 | set2)
print(set1 & set2)