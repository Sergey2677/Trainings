# Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
# # На вход этой функции передаются N длин сторон через аргументы.
# # Дополнительно могут быть указаны именованные аргументы:
# # type - булево значение True/False
# # color - целое числовое значение
# # closed - булево значение True/False
# # width - целое значение
# # Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в порядке их
# # перечисления в тексте задания (если они были переданы).
# # Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).
# # Функцию выполнять не нужно, только определить.

def get_data_fig(*args, **kwargs):
    values = [sum(args)]
    if 'type' in kwargs:
        values.append(kwargs['type'])
    if 'color' in kwargs:
        values.append(kwargs['color'])
    if 'closed' in kwargs:
        values.append(kwargs['closed'])
    if 'width' in kwargs:
        values.append(kwargs['width'])
    return tuple(values)



