class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, *args, **kwargs):
        return pow(args[0], 2) * self.a + args[0] * self.b + self.c
