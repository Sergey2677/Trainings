# Вводится строка целых чисел через пробел.
# Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# Sample Input:
# 5 6 3 6 -4 6 -1
# Sample Output:
# 26

s = input()

def dec_with_start_number(start=0):
    def calculate_sum(func):
        def wrapper(*args, **kwargs):
            return start + sum(func(*args,**kwargs))
        return wrapper
    return calculate_sum


@ dec_with_start_number(5)
def convert_str_to_list_of_ints(numbs):
    return list(map(int, numbs.split()))


print(convert_str_to_list_of_ints(s))