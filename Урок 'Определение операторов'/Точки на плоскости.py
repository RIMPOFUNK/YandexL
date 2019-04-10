class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.a != other.a or self.b != other.b:
            return True
        else:
            return False
