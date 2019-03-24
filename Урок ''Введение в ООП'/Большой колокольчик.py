class BigBell:
    def __init__(self):
        self.pr = False


    def sound(self):
        if not self.pr:
            print("ding")
            self.pr = True
        else:
            print('dong')
            self.pr = False