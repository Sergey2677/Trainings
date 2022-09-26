# Вводится строка, содержащая латинские символы, пробелы и цифры.
# Необходимо выделить из нее все неповторяющиеся цифры (символы от 0 до 9) и вывести на экран в одну строку через пробел их в порядке возрастания значений.
# Если цифры отсутствуют, то вывести слово НЕТ.
# Sample Input:
# Python 3.9.11 - best language!
# Sample Output:
# 1 3 9

# put your python code here

s = set(input())
digits = set()

for i in s:
    if i.isdigit():
        digits.add(i)

if len(digits) != 0:
    print(*sorted(digits))
else:
    print('НЕТ')