class SparseArray:
    def __init__(self):
        self.lst = dict()

    def __getitem__(self, key):
        if key in self.lst:
            return self.lst[key]
        else:
            return 0

    def __setitem__(self, key, item):
        self.lst[key] = item
