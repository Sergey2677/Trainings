# Вводятся две строки из слов (слова записаны через пробел).
# Объявите функцию, которая преобразовывает эти две строки в два списка слов и возвращает эти списки.
# Определите декоратор для этой функции, который из двух списков формирует словарь, в котором ключами являются слова из первого списка,
# а значениями - соответствующие элементы из второго списка.
# Полученный словарь должен возвращаться при вызове декоратора.
# Примените декоратор
# print(*sorted(d.items()))
# Sample Input:
# house river tree car
# дом река дерево машина
# Sample Output:
# ('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')

str = input()
str1 = input()

def convert_lists_to_dict(func):
    def wrapper(*args, **kwargs):
        lst, lst1 = func(*args, **kwargs)
        d = {}
        for i in range(len(lst1)):
            d[lst[i]] = lst1[i]
        return d

    return wrapper

@convert_lists_to_dict
def input_str_output_dict(str, str1):
    lst = str.split()
    lst1 = str1.split()
    return lst, lst1

print(*sorted(input_str_output_dict(str, str1).items()))