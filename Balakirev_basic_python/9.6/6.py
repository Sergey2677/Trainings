# На вход программы поступает список товаров в формате:
# название_1:цена_1
# ...
# название_N:цена_N
# Необходимо преобразовать этот список в словарь, ключами которого выступают цены (целые числа), а значениями - соответствующие названия товаров.
# Необходимо написать функцию, которая бы принимала на входе словарь и возвращала список из наименований трех наиболее дешевых товаров.
# Вызовите эту функцию и отобразите на экране полученный список в порядке возрастания цены в одну строчку через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# смартфон:120000
# яблоко:2
# сумка:560
# брюки:2500
# линейка:10
# бумага:500
# Sample Output:
# яблоко линейка бумага

# смартфон:120000 яблоко:2 сумка:560 брюки:2500 линейка:10 бумага:500

import sys


def best3(d):
    return [d[key] for key in sorted(d)[:3]]


lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
for s in lst_in:
    item, price = s.split(':')
    d[int(price)] = item

print(*best3(d))