class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i + 1):
                yield self.lst[i][j]

ls = [['1'], [2, 3], [4, 5, 6], ['7', 8, '9', 10]]
ls_one = [x for row in ls for x in row]

t = TriangleListIterator(ls)
for i, x in enumerate(t):
    assert x == ls_one[i], "итератор вернул неверное значение"