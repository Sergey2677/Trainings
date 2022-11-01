# data = p[indx] # получение данных по порядковому номеру (indx) атрибута
# # (порядок: fio, job, old, salary, year_job и начинается с нуля)
# p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
# for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
#     print(v)
import time


class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.order = list(self.__dict__.keys())
        self.pointer = 0

    def __check_index(self, index):
        if type(index) == int and 4 >= index >= 0:
            return self.order[index]
        else:
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        key = self.__check_index(item)
        return self.__dict__[key]

    def __setitem__(self, key, value):
        key = self.__check_index(key)
        self.__dict__[key] = value

    def __iter__(self):
        self.pointer = 0
        return self

    def __next__(self):
        while self.pointer <= 4:
            key = self.order[self.pointer]
            self.pointer += 1
            return self.__dict__[key]
        raise StopIteration
