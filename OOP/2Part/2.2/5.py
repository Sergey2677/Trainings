class WindowDlg:
    def __init__(self, title, width, height):
        self.__height = None
        self.__title = title
        self.__width = None
        self.width = width
        self.height = height

    def show(self) -> object:
        print(f"{self.__title}: {self.__width}, {self.height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) == int and 10000 >= width >= 0:
            if self.__width:
                self.show()
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) == int and 10000 >= height >= 0:
            if self.__height:
                self.show()
            self.__height = height

wnd = WindowDlg('ABC', 100, 100)
wnd.width = 200
wnd.height = 300
