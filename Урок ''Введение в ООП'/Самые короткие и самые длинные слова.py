class MinMaxWordFinder():


    def __init__(self):
        self.minword = 0
        self.maxword = 0
        self.list_word = []


    def add_sentence(self, text):
        self.list_word += text.split()
        try:
            self.minword = len(min(self.list_word, key=len))
            self.maxword = len(max(self.list_word, key=len))
        except ValueError:
            self.minword = 0
            self.maxword = 0


    def shortest_words(self):
        try:
            return sorted(list(filter(lambda x: len(x) == self.minword, self.list_word)))
        except ValueError:
            return []


    def longest_words(self):
        try:
            return sorted(set(filter(lambda x: len(x) == self.maxword, self.list_word)))
        except ValueError:
            return []

