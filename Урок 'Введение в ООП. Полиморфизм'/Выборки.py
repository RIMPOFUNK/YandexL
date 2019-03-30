class Selector:
    def __init__(self, values):
        self.odd = []
        self.evens = []
        for i in values:
            if i % 2 == 0:
                self.evens.append(i)
            else:
                self.odd.append(i)

    def get_odds(self):
        return self.odd

    def get_evens(self):
        return self.evens
