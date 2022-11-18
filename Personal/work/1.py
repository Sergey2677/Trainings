# 1. Посчитайте сумму всех четных и нечетных чисел в интервале от 100 до 1000

def counter(number_from: int, number_up_to: int) -> int:
    return sum([i for i in range(number_from, number_up_to) if i % 2 == 0])


print(counter(1, 10))
