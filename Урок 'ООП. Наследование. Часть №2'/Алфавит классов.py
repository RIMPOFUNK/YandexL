class A:
    def hello(self):
        print("Hello")

    def __str__(self):
        return "A.__str__ method"


class B:
    def good_evening(self):
        print("Good evening")

    def __str__(self):
        return "B.__str__ method"


class C(A, B):
    pass


class D(B, A):
    pass