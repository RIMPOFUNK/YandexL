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