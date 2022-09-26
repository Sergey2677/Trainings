# Вводятся данные в формате ключ=значение в одну строчку через пробел. Значениями здесь являются целые числа (см. пример ниже).
# Необходимо на их основе создать словарь d с помощью функции dict() и вывести его на экран командой: print(*sorted(d.items()))
# Sample Input: one=1 two=2 three=3
# Sample Output: ('one', 1) ('three', 3) ('two', 2)


# put your python code here

lst = [row.split('=') for row in input().split()]

d = dict(lst)

for i in d:
    d[i] = int(d[i])

print(*sorted(d.items()))