import sys
import time
import re

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def mul(m):
    m = m[4:-1]
    a, b = map(int, m.split(','))
    return a * b



def part_1(data):
    sum = 0
    for line in data:
        regex = "mul\([0-9]+,[0-9]+\)"
        matches = re.findall(regex, line)
        for m in matches:
            sum += mul(m)
    return sum

def part_2(data):
    sum = 0
    matches = []
    for line in data:
        regex = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
        matches.extend(re.findall(regex, line))
    
    active = True
    for m in matches:
        if m == "don't()":
            active = False
        elif m == "do()":
            active = True
        else:
            if active:
                sum += mul(m)
    
    return sum

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
