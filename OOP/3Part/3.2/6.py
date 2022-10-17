class RenderList:
    def __init__(self, type_list):
        if type_list == 'ol':
            self.type_list = type_list
        else:
            self.type_list = 'ul'

    def __call__(self, *args, **kwargs):
        return f'<{self.type_list}>\n<li>{args[0][0]}</li>\n<li>{args[0][1]}</li>\n<li>{args[0][2]}</li>\n</{self.type_list}>'

lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)

print(html)