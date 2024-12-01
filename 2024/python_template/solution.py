import sys
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


def part_1(data):
    return None

def part_2(data):
    return None

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")