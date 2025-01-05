# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros

# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
###
class Car:
    def __init__(self, name):
        self._name = name
        self._engine = None

    @property
    def name(self):
        return self._name

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value

###
class Engine:
    def __init__(self, name):
        self.name = name

###
class ManufactureCars:
    def __init__(self, name):
        self.name = name
        self._cars = []

    def add_car(self, car):
        self._cars.append(car)

    def show(self):
        for car in self._cars:
            print(f'Nome: {car.name} \nMotor: {car.engine.name} \nFabricante: {self.name}')

polo = Car("Polo")
polo_engine = Engine("1.2")
polo.engine = polo_engine

amarok = Car("Amarok")
amarok_engine = Engine("2.0 Turbo")
amarok.engine = amarok_engine

volkswagen = ManufactureCars("Volkswagen")
volkswagen.add_car(polo)
volkswagen.add_car(amarok)

volkswagen.show()