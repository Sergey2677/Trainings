from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def get_pk(self):
        ...

    def get_info(self):
        return f'Базовый класс Model'


class ModelForm(Model):
    _uid = 0

    def __new__(cls, *args, **kwargs):
        cls._uid += 1
        return super().__new__(cls)

    def __init__(self, login, password):
        self._login, self._password, self._id = login, password, self._uid

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())