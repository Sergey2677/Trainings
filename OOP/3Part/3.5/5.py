# эти строчки не менять
stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


class StripChars:
    def __init__(self, chars=''):
        self.chars = chars

    def __call__(self, lst):
        new_lst = []
        for i in lst:
            string = ''
            for j in i:
                if j not in self.chars:
                    string += j
            string = string.split()
            new_lst.append(string)
        return new_lst


class StringText:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)

st = StripChars("–?!,.;")
lst_text = [StringText(i) for i in st(stich)]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
lst_text_sorted = [' '.join(i.lst) for i in lst_text_sorted]