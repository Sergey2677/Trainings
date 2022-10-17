import re

class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))
        return wrapper

class RenderDigit:
    def __call__(self, *args, **kwargs):
        match = re.findall(r'^-?[0-9]*$', args[0])
        if match:
            return int(args[0])


input_dg = InputValues(RenderDigit())(input)
print(input_dg())
