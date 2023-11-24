from random import randint

class dice():
    def __init__(self, side = 6):
        self.side = side
    def roll(self):
        return randint(1,self.side)


