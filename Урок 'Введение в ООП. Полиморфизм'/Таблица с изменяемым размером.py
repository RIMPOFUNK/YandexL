"""class Table:
    def __init__(self, n, m):
        self.sizeN = n
        self.sizeM = m
        self.matrix = [[0 for i in range(m)] for j in range(n)]

    def set_value(self, i, j, value):
        self.matrix[i][j] = value

    def n_rows(self):
        return self.sizeN

    def n_cols(self):
        return self.sizeM

    def get_value(self, i, j):
        if i >= 0 and i < self.sizeN and j >= 0 and j < self.sizeM:
            return self.matrix[i][j]
        else:
            return None
    def add_col(self,col):

    def add_row(self,row):

tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
"""
# WRONG ANSWER
# AUTOR DANIL TRESHCHEV
