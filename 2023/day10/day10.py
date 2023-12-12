from enum import Enum
from typing import List


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class Tile:
    pipe_mapping = {
        "|": (Direction.NORTH, Direction.SOUTH),
        "-": (Direction.EAST, Direction.WEST),
        "L": (Direction.NORTH, Direction.EAST),
        "J": (Direction.NORTH, Direction.WEST),
        "7": (Direction.SOUTH, Direction.WEST),
        "F": (Direction.SOUTH, Direction.EAST),
        ".": None,
        "S": None,
    }

    char: str

    def __init__(self, char):
        self.char = char

    def getDirections(self):
        return self.pipe_mapping[self.char]


class Map:
    tiles: List[List[Tile]]

    def __init__(self, input_file) -> None:
        self.tiles = self.parse_input_file(input_file)

    def __str__(self) -> str:
        mapString = ""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                mapString += self.tiles[i][j].char
            mapString += "\n"
        return mapString

    def parse_input_file(self, input_file) -> List[List[Tile]]:
        first_dim = []
        with open(input_file) as input:
            second_dim = []
            for line in input.readlines():
                for char in line:
                    second_dim.append(Tile(char))
                first_dim.append(second_dim)
        return first_dim


def part1():
    map = Map("day10/sampleinput1.txt")
    print(map.__str__())
    print("hello")


def part2():
    print("hello")
