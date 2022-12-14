# 6. На входе многомерный список, каждый элемент содержит информацию о товаре,
# количестве и цене, которые были в каком-то заказе. Например: [[Товар1, 1,500],
# [Товар2, 7,1000],[Товар1, 6,900]]
# Вывести словарь:{Товар:Общая сумма заказа}


def func(lst_in):
    # Сформируем словарь с ключами
    d = {i[0]: 0 for i in lst_in}

    # Заполним значения
    for i in lst_in:
        if i[0] in d:
            d[i[0]] += i[1] * i[2]

    # Вернем словарь
    return d

lst_in = [['Товар1', 1, 500], ['Товар2', 7, 1000], ['Товар1', 6, 900]]

print(func(lst_in))
