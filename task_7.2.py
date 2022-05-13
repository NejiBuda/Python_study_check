"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
"""

class Clothes:
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    def param_V(self):
        return self.size / 6.5 + 0.5

    def param_H(self):
        return self.growth * 2 + 0.3

    @property
    def param_ALL(self):
        return str(f"Total tissue area is\n" f"{(self.size / 6.5 + 0.5)} + {(self.size / 6.5 + 0.5)}")


    class Coat(Clothes):
        def __init__(self, size, growth):
            super(Coat, self).__init__(size, growth)
            self.param_V = round(self.size / 6.5 + 0.5)

        def __str__(self):
            return f"For the coat you will need {self.param_V} fabrics"

    class Suit(Clothes):
        def __init__(self, size, growth):
            super(Suit, self).__init__(size, growth)
            self.param_H = round(self.growth * 2 + 0.3)

        def __str__(self):
            return f"For the coat you will need {self.param_H} fabrics"


coat = Coat(4, 7)
suit = Suit(3, 8)
print(coat)
print(suit)
print(coat.param_ALL)
print(siut.param_ALL)