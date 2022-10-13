from string import ascii_lowercase, digits


class TextInput:
    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
        CHARS_CORRECT = CHARS + CHARS.upper() + digits
        for i in name:
            if i not in CHARS_CORRECT:
                raise ValueError("некорректное поле name")
        if len(name) > 50 or len(name) < 3:
            raise ValueError("некорректное поле name")
        return True


class PasswordInput:
    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
            self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
        CHARS_CORRECT = CHARS + CHARS.upper() + digits
        for i in name:
            if i not in CHARS_CORRECT:
                raise ValueError("некорректное поле name")
        if len(name) > 50 or len(name) < 3:
            raise ValueError("некорректное поле name")
        return True

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()