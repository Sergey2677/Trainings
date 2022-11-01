# Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Необходимо на их основе создать словарь, затем проверить, существуют ли в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки).
# Если все они существуют, то вывести на экран ДА, иначе - НЕТ.
# Sample Input:
# вологда=город house=дом True=1 5=отлично 9=божественно
# Sample Output:
# ДА

# put your python code here
text = [i.split('=') for i in input().split()]

d = {i[0]: i[1] for i in text}

print('ДА' if 'house' in d and 'True' in d and '5' in d else 'НЕТ')