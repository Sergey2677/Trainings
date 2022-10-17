import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self, slot_1=None, slot_2=None, slot_3=None):
        self.slot_1 = slot_1
        self.slot_2 = slot_2
        self.slot_3 = slot_3

    def add_filter(self, slot_num, filtr):
        if slot_num == 1 and self.slot_1 is None and isinstance(filtr, Mechanical):
            self.slot_1 = filtr
        elif slot_num == 2 and self.slot_2 is None and isinstance(filtr, Aragon):
            self.slot_2 = filtr
        elif slot_num == 3 and self.slot_3 is None and isinstance(filtr, Calcium):
            self.slot_3 = filtr

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        elif slot_num == 2:
            self.slot_2 = None
        elif slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return (self.slot_1, self.slot_2, self.slot_3)

    def water_on(self):
        return all(f is not None and time.time() - f.date < self.MAX_DATE_FILTER for f in (self.slot_1, self.slot_2, self.slot_3))


class Mechanical:

    def __init__(self, date):
        self._date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        return


class Aragon:
    flag = False

    def __init__(self, date):
        self._date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        return


class Calcium:

    def __init__(self, date):
        self._date = date

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        return