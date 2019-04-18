def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Bishop:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour

    def can_move(self, row1, col1):
        if not correct_coords(row1, col1):
            return False
        if abs(self.row - row1) == abs(self.col - col1):
            return True
        else:
            return False

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.colour

    def char(self):
        return "B"