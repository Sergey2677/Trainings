# 7. Из задачи 6 постройте два списка идентификаторов товаров так, чтобы в каждом
# не было повторений.

lst_in = [['Товар1', 1, 500], ['Товар2', 7, 1000], ['Товар1', 6, 900]]


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


lst = [id(hash(CustomID(i))) for i in lst_in]
lst2 = [id(hash(CustomID2(i))) for i in lst_in]

# Если все id разные, длина сета будет 3
print(len(set(lst)) == 3)
print(len(set(lst2)) == 3)

# Проверка на наличие одинаковых id в разных сетах
print(set(lst).isdisjoint(set(lst2)))
