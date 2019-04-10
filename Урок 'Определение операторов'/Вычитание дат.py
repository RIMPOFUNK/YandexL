class Date:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
        self.prov = d2 - d1

    def __sub__(self, other):
        return self.prov - other.prov
