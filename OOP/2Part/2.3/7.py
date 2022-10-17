class ValidateString:
    """Проверка корректности переданной строки"""
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        """Возвращает True, если string является строкой (тип str) и длина строки в пределах [min_length; max_length]. Иначе возвращается False."""
        if type(string) == str:
            return self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator=ValidateString(min_length=3, max_length=100)):
        self.validator = validator

    def __set_name__(self, owner, item):
        self.item = "_" + item

    def __get__(self, instance, owner):
        return instance.__dict__[self.item]

    def __set__(self, instance, value):
        if self.validator.validate(value):
            instance.__dict__[self.item] = value

class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f"<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>")