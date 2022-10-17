# Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять к функциям следующим образом:
# @Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
# def contact(request):
#     return "Сергей Балакирев"
# Здесь аргумент methods декоратора Handler содержит список разрешенных запросов для обработки.
# Сама декорированная функция вызывается по аналогии с предыдущим подвигом:
# res = contact({"method": "POST", "url": "contact.html"})
# В результате функция contact должна возвращать строку в формате:
# "<метод>: <данные из функции>"
# В нашем примере - это будет:
# "POST: Сергей Балакирев"
# Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос.
# Если ключ method принимает значение отсутствующее в списке methods декоратора Handler, например, "PUT",
# то декорированная функция contact должна возвращать значение None.
# Для имитации GET и POST-запросов в классе Handler необходимо объявить два вспомогательных метода с сигнатурами:
# def get(self, func, request, *args, **kwargs) - для имитации обработки GET-запроса
# def post(self, func, request, *args, **kwargs) - для имитации обработки POST-запроса
# В зависимости от типа запроса должен вызываться соответствующий метод
# (его выбор в классе можно реализовать методом __getattribute__()).
# На выходе эти методы должны формировать строки в заданном формате.
# P.S. В программе достаточно объявить только класс. Ничего на экран выводить не нужно.

class Handler:
    def __init__(self, methods=('GET', )):
        self.methods = methods


    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            k = request.get('method', 'GET')
            if k in self.methods:
                method = k.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'