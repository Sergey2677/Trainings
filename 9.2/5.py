# Определите функцию-генератор, которая бы возвращала простые числа.
# (Простое число - это натуральное число, которое делится только на себя и на 1).
# Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.

from math import sqrt

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True

def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n

generator = prime_generator()

for i in range(20):
    print(next(generator))