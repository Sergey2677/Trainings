# Объявите функцию, которая возвращает переданную ей строку в нижнем регистре (с малыми буквами).
# Определите декоратор для этой функции, который имеет один параметр tag,
# определяющий строку с названием тега и начальным значением "h1".
# Этот декоратор должен заключать возвращенную функцией строку в тег tag и возвращать результат.
# Пример заключения строки "python" в тег h1: <h1>python</h1>
# Примените декоратор со значением tag="div" к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# Sample Input:
# Декораторы - это классно!
# Sample Output:
# <div>декораторы - это классно!</div>

s = input()

def dec_with_tag(tag='h1'):
    def dec_convert_lower(func):
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return dec_convert_lower


@dec_with_tag('div')
def convert_lower(s):
    return s.lower()

print(convert_lower(s))