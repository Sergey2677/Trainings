class PhoneBook:
    PHONES = []

    @classmethod
    def add_phone(cls, phone):
        cls.PHONES.append(phone)

    @classmethod
    def remove_phone(cls, index):
        cls.PHONES.pop(index)

    @classmethod
    def get_phone_list(cls):
        return cls.PHONES

class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)