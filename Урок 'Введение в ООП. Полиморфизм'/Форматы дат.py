class AmericanDate:
    def __init__(self, *args):
        args = list(args)
        if len(str(args[1])) == 1:
            args[1] = '0' + str(args[1])
        if len(str(args[2])) == 1:
            args[2] = '0' + str(args[2])
        self.forma = str(args[1]) + "." + str(args[2]) + "." + str(args[0])

    def format(self):
        return self.forma


class EuropeanDate:
    def __init__(self, *args):
        args = list(args)
        if len(str(args[1])) == 1:
            args[1] = '0' + str(args[1])
        if len(str(args[2])) == 1:
            args[2] = '0' + str(args[2])
        self.forma = str(args[2]) + "." + str(args[1]) + "." + str(args[0])

    def format(self):
        return self.forma