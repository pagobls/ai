import numpy as np
import random
import Orientation as orien


class Game:

    def __init__(self, n, seed=None):
        self.N = n
        self.chessboard = np.zeros((self.N, self.N), dtype=int, order='C')
        self.seed = seed
        Game.__spread_the_food(self)

    def __str__(self):
        return str(self.chessboard)

    def __spread_the_food(self):
        cont = 0
        random.seed(self.seed)
        while cont < self.N:
            r = random.randrange(0, self.N)
            c = random.randrange(0, self.N)
            if self.chessboard[r][c] == 1:
                continue
            else:
                self.chessboard[r][c] = 1
                cont += 1
        pass

    def print_field_of_game(self, row, col, orientation):
        for r in range(self.N):
            for c in range(self.N):
                if r == row and c == col:
                    if orientation == orien.Orientation.NORTH:
                        # print('\u2191', end='  ')
                        stri = '{0:4s}'.format('\u2191')
                        print(stri ,end='')
                    elif orientation == orien.Orientation.SOUTH:
                        # print('\u2193', end='  ')
                        stri = '{0:4s}'.format('\u2193')
                        print(stri ,end='')
                    elif orientation == orien.Orientation.EAST:
                        # print('\u2192', end='  ')
                        stri = '{0:4s}'.format('\u2192')
                        print(stri ,end='')
                    elif orientation == orien.Orientation.WEST:
                        # print('\u2190', end='  ')
                        stri = '{0:4s}'.format('\u2190')
                        print(stri ,end='')
                else:
                    # print(self.chessboard[r][c], end='  ')
                    stri = '{0:4s}'.format(str(self.chessboard[r][c]))
                    print(stri, end='')
            print(' ')
            print(' ')







