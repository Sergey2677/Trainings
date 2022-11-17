class Test:
    a = 1
    b = 2

    def func(self):
        for rec in self:
            print(rec)
        
a = Test()
a.func()
    

@property
def flag(self):
    return self.__flag
    
@flag.setter
def flag(self, flag):
    self.__flag = flag
    
