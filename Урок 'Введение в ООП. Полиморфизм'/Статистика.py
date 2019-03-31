class MinStat:
    def __init__(self):
        self.lst = []

    def add_number(self, number):
        self.lst.append(number)

    def result(self):
        try:
            return min(self.lst)
        except ValueError:
            return None


class MaxStat:
    def __init__(self):
        self.lst = []

    def add_number(self, number):
        self.lst.append(number)

    def result(self):
        try:
            return max(self.lst)
        except ValueError:
            return None


class AverageStat:
    def __init__(self):
        self.lst = []

    def add_number(self, number):
        self.lst.append(number)

    def result(self):
        try:
            return sum(self.lst) / len(self.lst)
        except ZeroDivisionError:
            return None
