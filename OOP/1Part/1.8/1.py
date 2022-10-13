# a learning assignment to design a network structure using OOP,
# check folder for task`s pdf file

from random import randint

class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """

    def __init__(self):
        self.buffer = []
        self.ip = self.generator_ip()

    @staticmethod
    def generator_ip():
        a = randint(0, 255)
        b = randint(0, 255)
        c = randint(0, 255)
        d = randint(0, 255)
        return f'{a}.{b}.{c}.{d}'


    @staticmethod
    def send_data(data):
        """для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя (пакет отправляется роутеру и
        сохраняется в его буфере - локальном свойстве buffer);
        """
        Router.buffer.append(data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список) и очищает входной буфер;
        """
        temp = self.buffer[:]
        self.buffer.clear()
        return temp

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.ip


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    buffer = []
    LINKS = []
    _instance = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            return cls._instance
        else:
            return cls._instance

    @classmethod
    def link(cls, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        cls.LINKS.append(server)

    @classmethod
    def unlink(cls, server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        cls.LINKS.remove(server)

    @classmethod
    def send_data(cls):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        for i in cls.buffer:
            for j in cls.LINKS:
                if i.ip == j.ip:
                    j.buffer.append(i)
        cls.buffer.clear()


class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip



router = Router()

sv_from = Server()
sv_from2 = Server()

router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)

sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))

router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_to)
print(msg_lst_from)