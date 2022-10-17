class Model:
    flag = False

    def query(self, *args, **kwargs):
        self.date = []
        for i in kwargs.items():
            self.date.append(f'{i[0]} = {i[1]}')
        self.flag = True

    def __str__(self):
        if self.flag:
            return "Model: " + f"{', '.join(self.date)}"
        else:
            return 'Model'

model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)

