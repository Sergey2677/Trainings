# На вход программы поступает строка из целых чисел, записанных через пробел.
# Напишите функцию get_list, которая преобразовывает эту строку в список из целых чисел и возвращает его.
# Определите декоратор для этой функции, который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
# print(*lst)
# Sample Input:
# 8 11 -5 4 3 10
# Sample Output:
# -5 3 4 8 10 11

s = input()

def sort_lst(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sorted(res)
    return wrapper

@sort_lst
def get_list(s):
    return list(map(int, s.split()))

lst = get_list(s)

print(*lst)