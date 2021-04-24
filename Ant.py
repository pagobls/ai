from Orientation import Orientation
from Direction import Direction
from Position import Position
from Game import Game
import math
import os


class Ant:

    def get_0_position(self):
        pos = Position(self.N)
        while self.grid.chessboard[pos.row][pos.col] == 1:
            pos = Position(self.N)

        return pos

    @staticmethod
    def make_directories(m):
        dir_name = 'output/train_set_m{}'.format(m)

        try:
            os.makedirs(dir_name)
            print("Creation of directory: directory", dir_name, "Created")
        except FileExistsError:
            print("Creation of directory: directory", dir_name, "already exists" + '\n')

    def __init__(self, m, n, seed=None):
        self.N = n
        self.m = m
        self.seed = seed
        self.score = 0
        self.n_of_moves = 0
        self.grid = Game(self.N, self.seed)
        self.position = self.get_0_position()
        self.orientation = Orientation.get_random_orientation()
        self.isAlive = True
        self.make_directories(m)
        # self.direction

    def move(self, dire):
        self.grid.chessboard[self.position.row][self.position.col] -= 1
        self.n_of_moves += 1

        if dire == Direction.UP:

            if self.orientation == Orientation.NORTH:

                self.position.row -= 1
                self.orientation = Orientation.NORTH

            elif self.orientation == Orientation.SOUTH:

                self.position.row += 1
                self.orientation = Orientation.SOUTH

            elif self.orientation == Orientation.EAST:

                self.position.col += 1
                self.orientation = Orientation.EAST

            elif self.orientation == Orientation.WEST:

                self.position.col -= 1
                self.orientation = Orientation.WEST

        elif dire == Direction.DOWN:

            if self.orientation == Orientation.NORTH:

                self.position.row += 1
                self.orientation = Orientation.SOUTH

            elif self.orientation == Orientation.SOUTH:

                self.position.row -= 1
                self.orientation = Orientation.NORTH

            elif self.orientation == Orientation.EAST:

                self.position.col -= 1
                self.orientation = Orientation.WEST

            elif self.orientation == Orientation.WEST:

                self.position.col += 1
                self.orientation = Orientation.EAST

        elif dire == Direction.RIGHT:

            if self.orientation == Orientation.NORTH:

                self.position.col += 1
                self.orientation = Orientation.EAST

            elif self.orientation == Orientation.SOUTH:

                self.position.col -= 1
                self.orientation = Orientation.WEST

            elif self.orientation == Orientation.EAST:

                self.position.row += 1
                self.orientation = Orientation.SOUTH

            elif self.orientation == Orientation.WEST:

                self.position.row -= 1
                self.orientation = Orientation.NORTH

        elif dire == Direction.LEFT:

            if self.orientation == Orientation.NORTH:

                self.position.col -= 1
                self.orientation = Orientation.WEST

            elif self.orientation == Orientation.SOUTH:

                self.position.col += 1
                self.orientation = Orientation.EAST

            elif self.orientation == Orientation.EAST:

                self.position.row -= 1
                self.orientation = Orientation.NORTH

            elif self.orientation == Orientation.WEST:

                self.position.row += 1
                self.orientation = Orientation.SOUTH

        self.eat()

    def look_around(self, orie):

        k = math.floor((2*self.m+1)/2)
        fow = []

        if orie == Orientation.NORTH:
            for r in range(-k, k+1):
                for c in range(-k, k+1):
                    if r == 0 and c == 0:
                        continue
                    else:
                        if self.position.row + r >= self.N or self.position.row + r < 0 or self.position.col + c >= self.N or self.position.col + c < 0:
                            fow.append(2)
                        else:
                            fow.append(self.grid.chessboard[self.position.row + r][self.position.col + c])

        elif orie == Orientation.SOUTH:
            for r in range(k, -k-1, -1):
                for c in range(k, -k-1, -1):
                    if r == 0 and c == 0:
                        continue
                    else:
                        if self.position.row + r >= self.N or self.position.row + r < 0 or self.position.col + c >= self.N or self.position.col + c < 0:
                            fow.append(2)
                        else:
                            fow.append(self.grid.chessboard[self.position.row + r][self.position.col + c])
        elif orie == Orientation.EAST:
            for c in range(k, -k-1, -1):
                for r in range(-k, k+1):
                    if r == 0 and c == 0:
                        continue
                    else:
                        if self.position.row + r >= self.N or self.position.row + r < 0 or self.position.col + c >= self.N or self.position.col + c < 0:
                            fow.append(2)
                        else:
                            fow.append(self.grid.chessboard[self.position.row + r][self.position.col + c])
        elif orie == Orientation.WEST:
            for c in range(-k, k+1):
                for r in range(k, -k-1, -1):
                    if r == 0 and c == 0:
                        continue
                    else:
                        if self.position.row + r >= self.N or self.position.row + r < 0 or self.position.col + c >= self.N or self.position.col + c < 0:
                            fow.append(2)
                        else:
                            fow.append(self.grid.chessboard[self.position.row + r][self.position.col + c])

        return fow

    def read_command_from_user(self, p):
        if p == 't':
            self.move(Direction.UP)
        elif p == 'v':
            self.move(Direction.DOWN)
        elif p == 'h':
            self.move(Direction.RIGHT)
        elif p == 'f':
            self.move(Direction.LEFT)
        else:
            print('Unable to move')

    def read_command_from_classifier(self, p, NN=False):

        if NN:
            if p == 3:
                self.move(Direction.UP)
            elif p == 0:
                self.move(Direction.DOWN)
            elif p == 2:
                self.move(Direction.RIGHT)
            elif p == 1:
                self.move(Direction.LEFT)
            else:
                print('Unable to move')

        else:

            if p == 'UP':
                self.move(Direction.UP)
            elif p == 'DOWN':
                self.move(Direction.DOWN)
            elif p == 'RIGHT':
                self.move(Direction.RIGHT)
            elif p == 'LEFT':
                self.move(Direction.LEFT)
            else:
                print('Unable to move')



    def eat(self):
        if self.position.row >= self.N or self.position.row < 0 or self.position.col >= self.N or self.position.col < 0:
            self.score += -(self.N+2)
            self.isAlive = False
            print('Game over!')
            print('your score:' + str(self.score))
            print('n_of_moves:'+ str(self.n_of_moves))
        else:
            self.score += self.grid.chessboard[self.position.row][self.position.col]
            if self.n_of_moves == 2*self.N:
                print('You survived!')
                print('your score:' + str(self.score))
                print('n_of_moves:' + str(self.n_of_moves))
                print('state of the ant: Alive')

    def draw_field_of_game(self):
        self.grid.print_field_of_game(self.position.row, self.position.col, self.orientation)
        # print('Your score: {}'.format(self.score))

    def print_on_a_file(self, p, num_of_matches):

        path = 'output/train_set_m{}/num_of_matches_{}.txt'.format(self.m, num_of_matches)

        with open(path, 'a') as f:

            if self.orientation == Orientation.NORTH:
                if p == 't':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                elif p == 'v':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)
                elif p == 'h':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)
                elif p == 'f':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

            elif self.orientation == Orientation.SOUTH:
                if p == 't':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                elif p == 'v':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)
                elif p == 'h':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)
                elif p == 'f':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

            elif self.orientation == Orientation.EAST:
                if p == 't':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                elif p == 'v':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)
                elif p == 'h':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)
                elif p == 'f':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

            elif self.orientation == Orientation.WEST:
                if p == 't':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                elif p == 'v':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)
                elif p == 'h':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)
                elif p == 'f':
                    for s in Orientation:
                        values = self.look_around(s)
                        if s == Orientation.NORTH:
                            moves = 'DOWN'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.SOUTH:
                            moves = 'UP'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.EAST:
                            moves = 'RIGHT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)

                        elif s == Orientation.WEST:
                            moves = 'LEFT'
                            for i in range(len(values)):
                                if i != len(values) - 1:
                                    st = '{},'.format(values[i])
                                    f.write(st)
                                else:
                                    st = '{},{}\n'.format(values[i], moves)
                                    f.write(st)



