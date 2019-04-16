class Summator:
    def __init__(self):
        self.n = 1
        self.b = 1

    def transform(self, n):
        self.n = n

    def sum(self, n):
        return sum([int(i) ** self.b for i in range(1, n + 1)])


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, b):
        self.b = b


class SquareSummator(PowerSummator):
    def __init__(self):
        self.b = 2

    def sum(self, n):
        return sum([int(i) ** self.b for i in range(1, n + 1)])


class CubeSummator(PowerSummator):
    def __init__(self):
        self.b = 3

    def sum(self, n):
        return sum([int(i) ** self.b for i in range(1, n + 1)])
