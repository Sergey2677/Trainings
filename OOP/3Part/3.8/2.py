class Record:
    def __init__(self, **kwargs):
        for i, j in kwargs.items():
            setattr(self, i, j)

    def __getitem__(self, item):
        try:
            key = list(self.__dict__.keys())[item]
            return self.__dict__[key]
        except:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        try:
            key = list(self.__dict__.keys())[key]
            self.__dict__[key] = value
        except:
            raise IndexError('неверный индекс поля')



r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r[1])