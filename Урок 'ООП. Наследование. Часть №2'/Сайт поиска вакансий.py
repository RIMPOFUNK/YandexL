class Profile:
    def __init__(self, name):
        self.name = name

    def info(self):
        return ''

    def describe(self):
        return self.info()


class Vacancy(Profile):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def info(self):
        return f"Предлагаемая зарплата: {self.money}"


class Resume(Profile):
    def __init__(self, name, sta):
        self.name = name
        self.sta = sta

    def info(self):
        return f"Стаж работы: {self.sta}"
