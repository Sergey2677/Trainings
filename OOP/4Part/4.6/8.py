class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request: dict):
        keys = ('url', 'method')
        if request.get(keys[1]) not in self.allowed_methods:
            raise TypeError(f"Метод {request.get(keys[1])} не разрешен.")
        method_request = request.get('method').lower()
        return self.__getattribute__(method_request)(request)  # имя метода, малыми буквами


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT',)


view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
print(html)