class Table:
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

    def add_col(self, col):
        for j in range(len(self.matrix)):
            self.matrix[j] = self.matrix[j][:col] + [0] + self.matrix[j][col:]
        self.sizeM += 1

    def add_row(self, row):
        self.matrix = self.matrix[:row] + list([[0 for i in range(self.sizeM)]
                                                for j in range(1)]) + self.matrix[row:]
        self.sizeN += 1

    def delete_row(self, row):
        self.matrix = self.matrix[:row] + self.matrix[row + 1:]
        self.sizeN -= 1

    def delete_col(self, col):
        for j in range(len(self.matrix)):
            self.matrix[j] = self.matrix[j][col:] + self.matrix[j][:col + 1]
        self.sizeM -= 1

tab = Table(8, 3)

tab.set_value(0, 0, 10)
tab.set_value(0, 1, 12)
tab.set_value(0, 2, 13)
tab.set_value(1, 2, 14)
tab.set_value(2, 2, 15)
tab.set_value(3, 2, 16)
tab.set_value(4, 2, 17)
tab.set_value(5, 2, 18)
tab.set_value(6, 2, 19)
tab.set_value(7, 2, 20)
tab.set_value(7, 1, 21)
tab.set_value(7, 0, 22)
tab.set_value(6, 0, 23)
tab.set_value(5, 0, 24)
tab.set_value(4, 0, 25)
tab.set_value(3, 0, 26)
tab.set_value(2, 0, 27)
tab.set_value(1, 0, 28)
tab.set_value(1, 1, 29)
tab.set_value(2, 1, 30)
tab.set_value(3, 1, 31)
tab.set_value(4, 1, 32)
tab.set_value(5, 1, 33)
tab.set_value(6, 1, 34)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.delete_row(4)
tab.delete_row(6)
tab.delete_col(2)
tab.add_row(2)

for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()