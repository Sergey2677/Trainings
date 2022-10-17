class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def  __setattr__(self, key, value):
        d = {
            'title': str,
            'author': str,
            'pages': int,
            'year': int
        }
        if d[key] != type(value):
            raise TypeError("Неверный тип присваиваемых данных.")
        return object.__setattr__(self, key, value)

book = Book('Сергей Балакирев', 'Python ООП', 123, 2022)