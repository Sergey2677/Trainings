import sys

# программу не менять, только добавить два метода
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a:b+1]

    def insert(self, data):
        for i in data:
            self.lst_data.append(dict(zip(self.FIELDS, i.split())))


db = DataBase()
db.insert(lst_in)

print(db.lst_data)