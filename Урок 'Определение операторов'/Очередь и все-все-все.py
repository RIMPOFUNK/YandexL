class Queue:
    def __init__(self, *args):
        self.lst = args
        self.lst = list(self.lst)

    def append(self, *args):
        for i in args:
            self.lst.append(i)

    def copy(self):
        return Queue(*self.lst)

    def pop(self):
        temp = self.lst[0]
        self.lst.remove(temp)
        return temp

    def extend(self, other):
        for i in other.lst:
            self.lst.append(i)

    def next(self):
        return Queue(*list(self.lst[1:]))

    def __str__(self):
        if len(self.lst) == 0:
            return "[]"
        result = "["
        for i in range(len(self.lst) - 1):
            result += f"{self.lst[i]} -> "
        result += str(self.lst[-1]) + "]"
        return result

    def __eq__(self, other):
        if self.lst == other.lst:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.lst == other.lst:
            return False
        else:
            return True

    def __add__(self, other):
        return Queue(*list(self.lst + other.lst))

    def __rshift__(self, n):
        return Queue(*self.lst[n:])

    def __call__(self, *args, **kwargs):
        return Queue(list(args[0].lst[1:]))

    def __next__(self):
        return Queue(*list(self.lst[1:]))
