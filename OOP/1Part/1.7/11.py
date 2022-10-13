class Viber:
    LST = []

    @classmethod
    def add_message(cls, msg):
        cls.LST.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.LST.remove(msg)

    @staticmethod
    def set_like(msg):
        msg.fl_like = True

    @classmethod
    def show_last_message(cls, number):
        for i in cls.LST[len(cls.LST) - number:]:
            print(i.text)

    @classmethod
    def total_messages(cls):
        return len(cls.LST)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like