# 9. Создайте класс. Пусть в нем будут поля Фамилия, Имя, Год рождения.
# 10. Создайте метод, который выводит ФИО.
# 11. Создайте метод, который вычисляет возраст в годах.
# 12. Создайте класс - наследник вашего первого класса. Перекройте в нём метод,
# вычисляющий возраст в годах на метод, который вычисляет возраст в днях.
# 13. Создайте декоратор для метода, который выводит ФИО. Пусть новый метод
# выводит ФИО, заключенное в теги <strong>.

import datetime


class FullName:
    def __init__(self, name, surname, year):
        self._name = name
        self._surname = surname
        if type(year) == int and 2022 > year > 1900:
            self._year = year
        else:
            raise ValueError("Возраст должен быть целым числом в диапазоне от 1900 до 2022")

    def show_age(self):
        now = datetime.datetime.now().year
        return now - self._year

    def decorator_fullname_with_tag(func):
        def wrapper(self):
            print('<strong>', end='')
            func(self)
            print('</strong>')

        return wrapper

    @decorator_fullname_with_tag
    def show_fullname(self):
        print(f'{self._name} {self._surname}', end='')


class FullNameInherit(FullName):
    def __init__(self, name, surname, year):
        super().__init__(name, surname, year)

    def show_age(self):
        some_date = datetime.datetime(self._year, 1, 1)
        now_date = datetime.datetime.now()
        res = now_date - some_date
        return str(res).split(',')[0]


obj = FullName('Sergey', 'Zheleznyakov', 1997)
obj.show_fullname()
# print()
obj = FullNameInherit('Sergey', 'Zheleznyakov', 1997)
print(obj.show_age())
