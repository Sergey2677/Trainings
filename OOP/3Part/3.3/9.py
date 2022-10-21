class Recipe:
    """
    Класс Recipe для представления рецептов,
    Отдельные ингредиенты рецепта должны определяться классом Ingredient
    len(recipe) - возвращает число ингредиентов в рецепте.
    """
    def __init__(self, *args, **kwargs):
        if args:
            self.ingredient = [*args]
        else:
            self.ingredient = []

    def add_ingredient(self, ing):
        """Добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец)"""
        self.ingredient.append(ing)

    def remove_ingredient(self, ing):
        """Удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта"""
        self.ingredient.remove(ing)

    def get_ingredients(self):
        """Получение кортежа из объектов класса Ingredient текущего рецепта"""
        return tuple(self.ingredient)

    def __len__(self):
        return len(self.ingredient)

class Ingredient:
    """
    В каждом объекте класса Ingredient должны создаваться локальные атрибуты:
    name - название ингредиента (строка);
    volume - объем ингредиента в рецепте (вещественное число);
    measure - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.
    """
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        """
        str(ing)  # "название: объем, ед. изм."
        """
        return f'{self.name}: {self.volume}, {self.measure}'


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3

print(n)