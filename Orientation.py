from enum import Enum
import random


class Orientation(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

    @classmethod
    def get_random_orientation(cls):
        v = random.randrange(1, 5)
        return cls(v)









