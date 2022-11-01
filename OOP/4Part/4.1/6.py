class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        else:
            return getattr(self, method.lower())(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError('request не является словарем')
        elif not request.get('url', False):
            raise TypeError('request не содержит обязательного ключа url')
        else:
            return f"url: {request.get('url')}"

dv = DetailView()
print(dv.render_request({'url': 'https://site.ru/home'}, 'GET'))   # url: https://site.ru/home