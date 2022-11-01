class ListInteger(list):
    def __init__(self, lst):
        for i in lst:
            if type(i) != int:
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(lst)

    @staticmethod
    def __check_type(item):
        if type(item) != int:
            raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        if self.__check_type(value):
            raise TypeError('можно передавать только целочисленные значения')
        else:
            super().__setitem__(key, value)
            
    def append(self, obj):
        self.__check_type(obj)
        super().append(obj)

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError