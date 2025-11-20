from abc import ABC, abstractmethod


class Rental(ABC):
    def __init__(self, rental_id):
        self._rental_id = rental_id

    @abstractmethod
    def calculate_rent(self, hrs):
        pass

    def __str__(self):
        return f' rental id : {self._rental_id}'
