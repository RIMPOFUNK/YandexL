﻿class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0


    def add_right(self, weight=0):
        self.right += weight


    def add_left(self, weight=0):
        self.left += weight


    def result(self):
        if self.left > self.right:
            return 'L'
        elif self.left < self.right:
            return 'R'
        else:
            return '='