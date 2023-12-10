import sys
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)

class Agent:
    def __init__(self, start_x, start_y, start_dir):
        self.x = start_x
        self.y = start_y
        self.steps = 0
        self.dir = start_dir


def find_start(pipe_map):
    for row_idx, row in enumerate(pipe_map):
        for col_idx, col in enumerate(row):
            if col == 'S':
                return col_idx, row_idx

def valid_coord(pipe_map, x, y):
    x_min, x_max = 0, len(pipe_map[0])
    y_min, y_max = 0, len(pipe_map)

    return (x >= x_min and x < x_max) and (y >= y_min and y < y_max)

def peek(pipe_map, x, y, dir):
    x_off, y_off = dir
    

def find_start_dirs(pipe_map, start_x, start_y):
    


def part_1(data):
    start_x, start_y = find_start(data)
    print(start_x, start_y)

def part_2(data):
    return None

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")