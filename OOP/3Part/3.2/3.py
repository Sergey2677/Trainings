class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self,*args, **kwargs):
        temp = args[0].split('.')
        return temp[-1] in self.extensions
