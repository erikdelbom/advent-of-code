import sys
import time
import numpy as np

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def find_start(data):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] in "<>^v":
                return y, x
    return -1, -1

def get_dir(c):
    if c == '<':
        return 0, -1
    elif c == '>':
        return 0, 1
    elif c == '^':
        return -1, 0
    elif c == 'v':
        return 1, 0
    else:
        print("Invalid direction character:", c)
        exit()

def rotate(c):
    if c == '<':
        return '^'
    elif c == '>':
        return 'v'
    elif c == '^':
        return '>'
    elif c == 'v':
        return '<'
    else:
        print("Invalid direction character:", c)
        exit()
     

def part_1(data):
    y, x = find_start(data)
    dir = data[y][x]
    visited = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    while True:
        dy, dx = get_dir(dir) 
        visited[y][x] = 1
        if y+dy >= len(data) or y+dy < 0 or x+dx >= len(data[0]) or x+dx < 0:
            break
        if data[y+dy][x+dx] == '#':
            dir = rotate(dir)
            dy, dx = get_dir(dir)
        
        y = y+dy
        x = x+dx
    
    visited = np.array(visited)
    return np.sum(visited)

def part_2(data):
    y, x = find_start(data)
    dir = data[y][x]
    visited = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    while True:
        dy, dx = get_dir(dir) 
        visited[y][x] = 1
        if y+dy >= len(data) or y+dy < 0 or x+dx >= len(data[0]) or x+dx < 0:
            break
        if data[y+dy][x+dx] == '#':
            dir = rotate(dir)
            dy, dx = get_dir(dir)
        
        y = y+dy
        x = x+dx
    
    visited = np.array(visited)
    return np.sum(visited)


input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
