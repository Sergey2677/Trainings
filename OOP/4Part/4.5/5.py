class Validator:
    def _is_valid(self, data):
        """
        :param data: Data to be checked
        :return: bool
        """
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value, self.max_value = min_value, max_value

    def _is_valid(self, data):
        return type(data) == float and self.max_value >= data >= self.min_value

    def __call__(self, data):
        return self._is_valid(data)


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])