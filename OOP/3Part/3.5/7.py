class FileAcceptor:
    def __init__(self, *args):
        self.ext = args

    def __call__(self, filename):
        for i in range(len(filename)-1, -1, -1):
            if filename[i] == '.':
                return filename[i+1:] in self.ext
        return False

    def __add__(self, other):
        s = set(self.ext) | set(other.ext)
        return FileAcceptor(*s)

filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames1 = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames1)

# assert filenames1 == ["boat.jpg", "web.png", "ava.base.jpg", "forest.jpeg",
#                      "eq_1.png"], "объекты класса FileAcceptor неверно отработали совместно с функцией filter"