class Clock:
    def __init__(self, tm=0):
        self.__time = tm

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        if type(tm) is int:
            return 100000 > tm >= 0
        return False


clock = Clock(4530)
