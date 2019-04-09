class Rectangle:
    def __init__(self, x, y, w, h):
        self.Left = x
        self.Top = y
        self.Width = w
        self.Height = h

    def intersection(self, r2):
        if isinstance(r2, Rectangle):
            self.tooLeft = self.Left > r2.Left + r2.Width
            self.tooRight = r2.Left > self.Left + self.Width
            self.tooHigh = self.Top > r2.Top + r2.Height
            self.tooLow = r2.Top > self.Top + self.Height
            return [r2.Left + r2.Width, self.Left + self.Width, r2.Top + r2.Height, self.Top + self.Height]


rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)
print(rect3)
