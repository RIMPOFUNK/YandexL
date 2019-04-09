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
            self.matrix[j] = self.matrix[j][:col] + self.matrix[j][col + 1:]
        self.sizeM -= 1


