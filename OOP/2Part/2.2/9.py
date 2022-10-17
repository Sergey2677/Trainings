import math

class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:

    def __init__(self, *args):
        self.LINES = list((LineTo(0, 0),) + args)

    def get_path(self):
        return self.LINES[1:]

    def get_length(self):
        """L = sqrt((x1-x0)^2 + (y1-y0)^2)"""
        coords = ((self.LINES[i - 1], self.LINES[i]) for i in range(1, len(self.LINES)))
        res = sum(map(lambda x: math.sqrt(pow((x[0].x - x[1].x), 2) + pow((x[0].y - x[1].y), 2)), coords))
        return res

    def add_line(self, line):
        self.LINES.append(line)


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()

print(dist)
