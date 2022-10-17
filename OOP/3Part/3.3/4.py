class WordString:
    def __init__(self, string=''):
        self.__string = string

    def __len__(self):
        return len(self.__string.split())

    def __call__(self, indx):
        return self.__string.split()[indx]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string):
        self.__string = string

words = WordString()
words.string = "Курс по Python    ООП от  Сергея Балакирева"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")


assert words.string == "Курс по Python    ООП от  Сергея Балакирева", "объект-свойство string вернуло невереные данные"