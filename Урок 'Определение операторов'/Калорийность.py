class FoodInfo:
    def __init__(self, *args):
        self.proteins = args[0]
        self.fats = args[1]
        self.carbohydrates = args[2]
        self.kcalories = args[0] * 4 + 9 * args[1] + 4 * args[2]

    def __add__(self, other):
        return FoodInfo(self.proteins + other.proteins, self.fats + other.fats,
                        self.carbohydrates + other.carbohydrates)

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        return self.kcalories
