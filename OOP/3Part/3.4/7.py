# Также объекты класса Lib должны работать со следующими операторами:
# lib = lib + book # добавление новой книги в библиотеку
# lib += book
# lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
# lib -= book
# lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= indx
# При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.

class Lib:
    """
    Для представления библиотеки в целом
    Объекты класса Lib создаются командой:
    lib = Lib()
    Каждый объект должен содержать локальный публичный атрибут:
    book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой
    Также с объектами класса Lib должна работать функция:
    n = len(lib) # n - число книг"""

    def __init__(self, book_list=None):
        self.book_list = book_list[:] if book_list and type(book_list) == list else []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        else:
            self.book_list.pop(other)
        return self


class Book:
    """
    Для описания отдельной книги
    Объекты класса Book должны создаваться командой:
    book = Book(title, author, year)
    где:
    title - заголовок книги (строка);
    author - автор книги (строка);
    year - год издания (целое число)"""

    def __init__(self, title, author, year):
        self.title= title
        self.author = author
        self.year = year
