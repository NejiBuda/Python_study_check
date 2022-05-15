from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Suit(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"

class Suit(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)

class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


coat = Coat(48)
suit = Suit(180)
print(coat + suit + coat)



