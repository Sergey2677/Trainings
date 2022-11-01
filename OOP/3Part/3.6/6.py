class ShopItem:
    def __init__(self, name, weight, price):
        self.name, self.weight, self.price = name, weight, price

    def __hash__(self):
        return hash((self.name, self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ['Системный блок: 1500 75890.56', 'Монитор Samsung: 2000 34000', 'Клавиатура: 200.44 545', 'Монитор Samsung: 2000 34000']
shop_items = dict()
for i in lst_in:
    j = i.split(':')
    j1 = j[1].split()
    obj = ShopItem(j[0], *j1)
    if shop_items.get(obj) is None:
        shop_items[obj] = [obj, 1]
    else:
        shop_items[obj][1] += 1