class AppStore:
    lst = []

    def add_application(self, app):
        self.lst.append(app)
    def remove_application(self, app):
        index = self.lst.index(app)
        del self.lst[index]
    def block_application(self, app):
        app.blocked = True
    def total_apps(self):
        return len(self.lst)

class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked