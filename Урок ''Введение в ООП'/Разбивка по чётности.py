class OddEvenSeparator:
    def __init__(self):
        self.even1 = []
        self.odd1 = []


    def add_number(self, number=0):
        if number % 2 == 0:
            self.even1.append(number)
        else:
            self.odd1.append(number)


    def odd(self):
        return self.odd1


    def even(self):
        return self.even1