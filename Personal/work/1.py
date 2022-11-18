# 1. Посчитайте сумму всех четных и нечетных чисел в интервале от 100 до 1000

def counter(number_from: int, number_up_to: int) -> int:
    odd = sum([i for i in range(number_from, number_up_to) if i % 2 == 0])
    even = sum([i for i in range(number_from, number_up_to) if i % 2 == 1])
    return odd + even


print(counter(1, 10))
