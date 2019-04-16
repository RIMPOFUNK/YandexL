class Summator:
    def transform(self, n):
        self.n = n

    def sum(self, n):
        return sum([int(i) for i in range(1, n + 1)])


class SquareSummator(Summator):
    def sum(self, n):
        return sum([int(i) ** 2 for i in range(1, n + 1)])


class CubeSummator(Summator):
    def sum(self, n):
        return sum([int(i) ** 3 for i in range(1, n + 1)])
