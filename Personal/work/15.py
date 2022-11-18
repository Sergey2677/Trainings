# Напишите программу, которая определяет, какой сегодня работает контроллер и в
# зависимости от этого какую следует выбрать функцию проверки продукции, если
# заранее известно, что кусок кода, который отвечает за сам процесс оценки, в
# будущем менять нельзя, например потому, что этот код будет упакован в релиз или
# подлежит обязательной сертификации, а дату оценки нельзя передать в качестве
# параметра.
# Например:
# ...какой-то код…
# return check_good(good)
# ...какой-то код…...


day, lst = input("Day, product [example: 21, 1000(or list)]: ").split(',')


def check_product(day, lst):
    d = {
        0: [1000, 1100],  # Четный
        1: [950, 1050]  # Нечетный
    }

    if type(lst) == list:
        ...

    else:
        return int(lst) in range(d[day][0], d[day][1])


def func1(day, lst):
    day = int(day) % 2
    return check_product(day, lst)


print(func1(day, lst))
