# 14. Отсортируйте список из задачи 6 по: товару, по сумме в строке (количество*цену).
# Используйте для сортировки лямда функцию.

from operator import attrgetter


lst_in = [['Товар1', 1, 500], ['Товар2', 7, 1000], ['Товар1', 6, 900]]

lst_in.sort(key=lambda x: (x[0], x[1]*x[2]))

print(lst_in)