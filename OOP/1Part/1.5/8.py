# Объявите в программе класс Cart (корзина), объекты которого создаются командой:
# cart = Cart()
# Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки
# (объекты классов Table, TV, Notebook и Cup).
# Изначально этот список должен быть пустым.
# В классе Cart объявить методы:
# add(self, gd) - добавление в корзину товара, представленного объектом gd;
# remove(self, indx) - удаление из корзины товара по индексу indx;
# get_list(self) - получение из корзины товаров в виде списка из строк:
# ['<наименовние_1>: <цена_1>',
# '<наименовние_2>: <цена_2>',
# ...
# '<наименовние_N>: <цена_N>']
# Объявите в программе следующие классы для описания товаров:
# Table - столы;
# TV - телевизоры;
# Notebook - ноутбуки;
# Cup - кружки.
# Объекты этих классов должны создаваться командой:
# gd = ИмяКласса(name, price)
# Каждый объект классов товаров должен содержать локальные свойства:
# name - наименование;
# price - цена.
# Создайте в программе объект cart класса Cart.
# Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup).
# Названия и цены придумайте сами.
# P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        '''добавление в корзину товара, представленного объектом gd'''
        self.goods.append(gd)

    def remove(self, indx):
        '''удаление из корзины товара по индексу indx'''
        del self.goods[indx]

    def get_list(self):
        '''получение из корзины товаров в виде списка из строк'''
        lst = []
        for i in self.goods:
            lst.append(f'{i.name}: {i.price}')
        return lst


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

tv = TV('Samsung', 50000)
cart.add(tv)
tv1 = TV('Sony', 50000)
cart.add(tv1)

table = TV('Wooden', 15000)
cart.add(table)

notebook1 = Notebook('HP', 55000)
cart.add(notebook1)
notebook2 = Notebook('Asus', 85000)
cart.add(notebook2)

cup = Cup('Noname', '1000')
cart.add(cup)
