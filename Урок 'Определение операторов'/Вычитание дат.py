class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day
        self.months = {31: (1, 3, 5, 7, 8, 10, 12), 30: (4, 6, 9, 11), 28: (2,)}
        self.days_from_start_year = self.__get_days_count()

    def __sub__(self, other):
        return self.days_from_start_year - other.days_from_start_year

    def __get_days_count(self):
        result = 0
        for month in range(1, self.month):
            for k, v in self.months.items():
                if month in v:
                    result = result + k
                    break
        result += self.day
        return result
