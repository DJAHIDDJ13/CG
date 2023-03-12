from enum import Enum
import sys
from typing import List, Tuple
import time

class MapItem(Enum):
    EMPTY = 0
    START = 1
    SUICIDE_BOOTH = 2
    WALL = 3
    OBSTACLE = 4
    TELEPORTER = 5
    CIRCUIT_INVERTER = 6
    PATH_MODIFIER_W = 7
    PATH_MODIFIER_E = 8
    PATH_MODIFIER_N = 9
    PATH_MODIFIER_S = 10
    BEER = 11

    @classmethod
    def from_symbol(cls, symb):
        SYMBOL_ITEM_MAPPING = {
            ' ': "EMPTY",
            "@": "START",
            "$": "SUICIDE_BOOTH",
            "T": "TELEPORTER",
            "#": "WALL",
            "X": "OBSTACLE",
            "I": "CIRCUIT_INVERTER",
            "W": "PATH_MODIFIER_W",
            "E": "PATH_MODIFIER_E",
            "N": "PATH_MODIFIER_N",
            "S": "PATH_MODIFIER_S",
            "B": "BEER",
        }
        return cls[SYMBOL_ITEM_MAPPING[symb]]

    def __repr__(self):
        ITEM_SYMBOL_MAPPING = {
            "EMPTY": ' ',
            "START": "@",
            "SUICIDE_BOOTH": "$",
            "TELEPORTER": "T",
            "WALL": "#",
            "OBSTACLE": "X",
            "CIRCUIT_INVERTER": "I",
            "PATH_MODIFIER_W": "W",
            "PATH_MODIFIER_E": "E",
            "PATH_MODIFIER_N": "N",
            "PATH_MODIFIER_S": "S",
            "BEER": "B",
        }
        return ITEM_SYMBOL_MAPPING[self.name]
    __str__ = __repr__

class BlunderDirection(Enum):
    SOUTH = (0, 1)
    WEST = (-1, 0)
    NORTH = (0, -1)
    EAST = (1, 0)
    @classmethod
    def from_symbol(cls, symb):
        SYMBOL_DIRECTION_MAPPING = {
            'S': 'SOUTH',
            'E': 'EAST',
            'N': 'NORTH',
            'W': 'WEST',            
        }
        return cls[SYMBOL_DIRECTION_MAPPING[symb]]

class CityMap:
    def __init__(self, width, height):
        self.map = [[MapItem.EMPTY for x in range(width)] for y in range(height)]
        # storing obstacles since they can be broken when in breaker_mode
        # This will allow us to generate a unique hash of the changes to the city map
        self.obstacles_coords = []
        # this is going to be an integer but we'll use the bits in its binary repr as booleans for each coord
        self.obstacles_broken = 0 

    def __getitem__(self, coord: Tuple[int, int]) -> MapItem:
        x, y = coord
        return self.map[y][x]

    def __setitem__(self, coord: Tuple[int, int], item: MapItem):
        if (self[coord], item) == (MapItem.EMPTY, MapItem.OBSTACLE):
            # if we're adding a new obstacle add it to the list
            self.obstacles_coords.append(coord)

        if (self[coord], item) == (MapItem.OBSTACLE, MapItem.EMPTY):
            # if an obstacle got destroyed (OBSTACLE -> EMPTY) Change its state in obstacles_broken
            # by doing bitwise and with the bit at index obstacle_idx
            obstacle_idx = self.obstacles_coords.index(coord)
            self.obstacles_broken |= (1 << obstacle_idx)

        x, y = coord
        self.map[y][x] = item

    def __repr__(self) -> str:
        lines = []
        for line in self.map:
            items_str = [str(e) for e in line]
            lines.append(''.join(items_str))
        return "\n".join(lines)

    def __hash__(self) -> int:
        return self.obstacles_broken

class BlunderSim:
    def __init__(self, start: Tuple[int, int], end: Tuple[int, int], city_map: CityMap):
        self.cur_pos = start
        self.direction = 0 # idx in direction_priority
        self.direction_increment = 1
        self.city_map = city_map
        self.breaker_mode = False
        self.direction_priority = (
            BlunderDirection.SOUTH,
            BlunderDirection.EAST,
            BlunderDirection.NORTH,
            BlunderDirection.WEST,
        )        
        self.teleporters = {}
        self.finished = False

    @classmethod
    def from_input(cls):
        l, c = map(int, input().split())
        width, height = c, l
        start = None
        end = None
        teleporters = []
        city_map = CityMap(width, height)
        for y in range(height):
            row = input().strip()
            for x, item in enumerate(row):
                if item == '@':
                    start = (x, y)
                    item = ' '
                elif item == '$':
                    end = (x, y)
                elif item == 'T':
                    teleporters.append((x, y))

                city_map[(x, y)] = MapItem.from_symbol(item.upper())
    
        assert len(teleporters) in [0, 2]

        obj = cls(start, end, city_map)
        for a, b in zip(teleporters[::2], teleporters[1::2]):
            obj.add_teleporter(a, b)

        return obj

    def add_teleporter(self, coord1: Tuple[int, int], coord2: Tuple[int, int]):
        self.city_map[coord1] = MapItem.TELEPORTER  
        self.city_map[coord2] = MapItem.TELEPORTER
        self.teleporters[coord1] = coord2
        self.teleporters[coord2] = coord1

    def step(self):
        # in place modifications
        cur_item = self.city_map[self.cur_pos]
        new_dir = self.direction
        if cur_item == MapItem.BEER:
            self.breaker_mode = not self.breaker_mode
        elif cur_item == MapItem.CIRCUIT_INVERTER:
            self.direction_increment *= -1 # invert the increment direction
        elif cur_item.name.startswith("PATH_MODIFIER"):
            new_dir = cur_item.name[-1] # the last char is the direction
            self.direction = self.direction_priority.index(BlunderDirection.from_symbol(new_dir))
        elif cur_item == MapItem.SUICIDE_BOOTH:
            self.finished = True
            return True, None
        elif cur_item == MapItem.TELEPORTER:
            self.cur_pos = self.teleporters[self.cur_pos] # teleport to position of other teleporter


        # if we're about to encounter an obstacle, reset the direction
        dx, dy = self.direction_priority[self.direction].value
        new_pos = (self.cur_pos[0] + dx, self.cur_pos[1] + dy)
        new_item = self.city_map[new_pos]
        if new_item == MapItem.WALL or (new_item == MapItem.OBSTACLE and not self.breaker_mode):
            self.direction = 0 if self.direction_increment == 1 else 3

        chosen_dir = None
        # check next potential positions starting from enforced path modifier if necessary
        start_dir = self.direction
        for i in range(len(self.direction_priority)):
            d = (start_dir + i * self.direction_increment) % len(self.direction_priority)
            chosen_dir = self.direction_priority[d].name
            dx, dy = self.direction_priority[d].value
            new_pos = (self.cur_pos[0] + dx, self.cur_pos[1] + dy)
            new_item = self.city_map[new_pos]
            if new_item == MapItem.WALL:
                continue
            elif new_item == MapItem.OBSTACLE:
                if not self.breaker_mode:
                    continue
                else:
                    self.city_map[new_pos] = MapItem.EMPTY
            # if the next position is not blocked, move to it
            self.cur_pos = new_pos
            self.direction = d
            break

        return False, chosen_dir

    def __hash__(self):
        return hash((hash(self.city_map), self.cur_pos, self.direction, self.direction_increment, self.breaker_mode, self.finished))

    def __repr__(self):
        city_map = [[c for c in line] for line in str(self.city_map).split("\n")]
        city_map[self.cur_pos[1]][self.cur_pos[0]] = '@'
        return '\n'.join(map(''.join, city_map))


if __name__ == "__main__":
    blunder_sim = BlunderSim.from_input()
    blunder_history = set()
    moves = []
    i = 0
    running = True
    while running and i < 10_000:
        #print("\033c", end='', file=sys.stderr)
        #print(blunder_sim, file=sys.stderr)
        blunder_history.add(hash(blunder_sim))
        finished, move = blunder_sim.step()
        if not finished: moves.append(move)
        running = not finished and hash(blunder_sim) not in blunder_history
        i += 1
        #time.sleep(2)
    if hash(blunder_sim) not in blunder_history:
        print(*moves, sep="\n")
    else:
        print('LOOP')