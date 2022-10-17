import random

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join(random.choice(self.psw_chars) for i in range(random.randint(self.min_length, self.max_length)))

lst_pass = [RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)() for i in range(3)]
print(lst_pass)


def short_circuit(psw_chars, min_length, max_length):
    def generate_passw():
        return ''.join(random.choice(psw_chars) for i in range(random.randint(min_length, max_length)))
    return generate_passw

a = short_circuit("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 20, 20)
b = short_circuit("qwertyuio", 5, 5)
print(a())
print(b())