from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make, model, price):
        self._make = make
        self._model = model
        self._price = price

    @abstractmethod
    def calculate_premium(self):
        pass

    def __str__(self):
        return f'Vehicle details make : {self._make}, model : {self._model},' \
               f' price : {self._price}'


class Car(Vehicle):
    def __init__(self, make, model,price, segment='standard'):
        super().__init__(make, model, price)
        self._segment = segment

    def calculate_premium(self):
        if self._segment == 'luxury':
            return self._price * 0.025
        else:
            return self._price * 0.020

    def __str__(self):
        return super().__str__() + f' segment : {self._segment}'


class Bike(Vehicle):

    def __init__(self, make, model, price):
        super().__init__(make, model, price)

    def calculate_premium(self):
        return self._price * 0.015


