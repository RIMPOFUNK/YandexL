class AmericanDate:
    def __init__(self, *args):
        self.year = args[0]
        self.month = args[1]
        self.day = args[2]
        self.result = format(self)

    def set_year(self, year):
        self.year = year
        self.result = format(self)

    def set_month(self, month):
        self.month = month
        self.result = format(self)

    def set_day(self, day):
        self.day = day
        self.result = format(self)

    def format(self):
        if len(str(self.day)) == 1:
            self.day = '0' + str(self.day)
        if len(str(self.month)) == 1:
            self.month = '0' + str(self.month)
        return str(self.month) + "." + str(self.day) + "." + str(self.year)

    def get_month(self):
        if self.month[0] == "0":
            return self.month[1]
        return self.month

    def get_day(self):
        if self.day[0] == "0":
            return self.day[1]
        return self.day

    def get_year(self):
        return self.year


class EuropeanDate:
    def __init__(self, *args):
        self.year = args[0]
        self.month = args[1]
        self.day = args[2]
        self.result = format(self)

    def set_year(self, year):
        self.year = year
        self.result = format(self)

    def set_month(self, month):
        self.month = month
        self.result = format(self)

    def set_day(self, day):
        self.day = day
        self.result = format(self)

    def format(self):
        if len(str(self.day)) == 1:
            self.day = '0' + str(self.day)
        if len(str(self.month)) == 1:
            self.month = '0' + str(self.month)
        return str(self.day) + "." + str(self.month) + "." + str(self.year)

    def get_month(self):
        if self.month[0] == "0":
            return self.month[1]
        return self.month

    def get_day(self):
        if self.day[0] == "0":
            return self.day[1]
        return self.day

    def get_year(self):
        return self.year
