class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if "method" not in args[0].keys():
            return f"GET: {self.func(args)}"
        elif args[0]['method'] != 'GET':
            return None
        else:
            return f"{args[0]['method']}: {self.func(args)}"

@HandlerGET
def index(request):
    return "главная страница сайта"

