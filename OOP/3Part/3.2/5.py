import re

class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        match = re.findall(r'^-?[0-9]*$', args[0])
        if match:
            return int(args[0])

dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]

print(digits)
