class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model, self._mass, self._speed, self._top = model, mass, speed, top

    def __setattr__(self, key, value):
        if key == '_model' and type(value) != str:
            raise TypeError('неверный тип аргумента')
        elif key == '_mass' or key == '_speed' or key == '_top':
            if type(value) not in (int, float):
                raise TypeError('неверный тип аргумента')
            elif type(value) in (int, float) and value <= 0:
                raise TypeError('неверный тип аргумента')
        object.__setattr__(self, key, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, key, value):
        if key == "_chairs" and type(value) != int:
            raise TypeError('неверный тип аргумента')
        elif key == "_chairs" and type(value) == int and value <= 0:
            raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, key, value):
        if key == "_weapons" and type(value) != dict:
            raise TypeError('неверный тип аргумента')
        super().__setattr__(key, value)

planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]