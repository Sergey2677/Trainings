# Вводятся пункты меню (каждый пункт с новой строки) в формате:
# название_1 URL-адрес_1
# название_2 URL-адрес_2
# ...
# название_N URL-адрес_N
# Необходимо эту информацию представить в виде вложенного кортежа menu в формате:
# ((название_1, URL-адрес_1), (название_2, URL-адрес_2), ... (название_N, URL-адрес_N))
# Результат вывести на экран в виде кортежа командой:
# print(menu)
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# Sample Input:
# Главная home
# Python learn-python
# Java learn-java
# PHP learn-php
# Sample Output:
# (('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))

lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']

lst_in = [i.split() for i in lst_in]

t = ((lst_in[i][0], lst_in[i][1]) for i in range(len(lst_in)))

print(tuple(t))