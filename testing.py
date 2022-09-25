class Person:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('Type must be a string')
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Incorrect recording format")
        for item in f:
            if not item.isalpha():
                raise TypeError("Should consist only of letters of the alphabet")
            if len(item) < 1:
                raise TypeError("Length of fullname should be more than 1")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Old must be an integer between 14 and 120")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Weight should be real number from 20 and more")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Passport should be a string")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Incorrect passport format ")

        for item in s:
            if not item.isdigit():
                raise TypeError("Serial and number of passport should be integer")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p = Person('Zheleznyakov Sergey Vyacheslavovich', 14, "2717 666861", 72.4)
print(p.__dict__)
