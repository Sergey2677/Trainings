# Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:
#
# a = SingletonFive(<наименование>)
# Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.
#
# Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.) должны быть ссылкой на последний (пятый) созданный объект.
#
# Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# P.S. В программе на экран ничего выводить не нужно.


class SingletonFive:
    counter_objects = 0
    link_to_fifth_object = None

    def __new__(cls, *args, **kwargs):
        if cls.counter_objects < 3:
            cls.counter_objects += 1
            return super().__new__(cls)
        elif cls.counter_objects == 3:
            cls.link_to_fifth_object = super().__new__(cls)
            cls.counter_objects += 1
            return super().__new__(cls)
        else:
            return cls.link_to_fifth_object

    def __init__(self, name):
        self.name = name

objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять

for i in objs:
    print(id(i))