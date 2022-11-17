from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def population(self):
        ...

    @property
    @abstractmethod
    def square(self):
        ...


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name, self._population, self._square = name, population, square

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        if type(population) != int:
            raise ValueError
        self._population = population

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, square):
        if type(square) not in (float, int):
            raise ValueError
        self._square = square


    def get_info(self):
        return f'{self.name}: {self.square}, {self.population}'


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000