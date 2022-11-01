# Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной в N символов.
# Например, при N=6, получим адрес: SCrUZo@mail.ru
# Для формирования случайного индекса для строки chars используйте функцию randint модуля random:
# import random
# random.seed(1)
# indx = random.randint(0, len(chars)-1)
# Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно.
# Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
# Sample Input:
# 8
# Sample Output:
# iKZWeqhF@mail.ru
# WCEPyYng@mail.ru
# FbyBMWXa@mail.ru
# SCrUZoLg@mail.ru
# ubbbPIay@mail.ru

from string import ascii_lowercase, ascii_uppercase
import random

chars = ascii_lowercase + ascii_uppercase

def get_random_email(N):
    rand_string = ''.join(random.choice(chars) for i in range(N))
    email = rand_string + '@mail.ru'
    yield email


N = int(input())

for i in range(5):
    email = get_random_email(N)
    print(next(email))
