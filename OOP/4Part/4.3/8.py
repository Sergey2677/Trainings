class SoftList(list):
    def __init__(self, lst):
        super().__init__(lst)
    """чтобы при обращении к несуществующему элементу (по индексу) возвращалось значение False (а не исключение Out of Range"""
    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except:
            return False


sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
sl[6] # False
sl[-7] # False