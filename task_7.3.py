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