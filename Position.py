import random


class Position:

    def __init__(self, n):
        self.row = random.randrange(0, n)
        self.col = random.randrange(0, n)

    def __str__(self):
        return 'r:{} c:{}'.format(self.row, self.col)
