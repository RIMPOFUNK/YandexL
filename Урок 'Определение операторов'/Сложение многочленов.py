class Polynomial:
    def __init__(self, lst):
        self.lst = lst

    def __call__(self, x):
        s = 0
        for i in range(len(self.lst)):
            s += self.lst[i] * pow(x, i)
        return s

    def __add__(self, other):
        st = []
        temp = Polynomial(st)
        if len(self.lst) < len(other.lst):
            m = len(self.lst)
        else:
            m = len(other.lst)
        for i in range(m):
            st.append(self.lst[i] + other.lst[i])
        if len(self.lst) > m:
            st += self.lst[m::]
        else:
            st += other.lst[m::]
        temp.lst = st
        return temp
