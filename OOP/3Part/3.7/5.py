import sys


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def recieve(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for i in (MailItem(*i.split("; ")) for i in lst_in):
            self.inbox_list.append(i)


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


mail = MailBox()
mail.recieve()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))

for i in inbox_list_filtered:
    print(i.is_read)
