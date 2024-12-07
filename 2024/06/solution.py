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

get_offset = {'<': (0, -1), '>': (0, 1), '^':(-1, 0), 'v': (1, 0)}
rotate = {'<': '^', '>': 'v', '^': '>', 'v': '<'}

def part_1(data):
    y, x = find_start(data)
    dir = data[y][x]
    visited = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    while True:
        dy, dx = get_offset[dir] 
        visited[y][x] = 1
        if y+dy >= len(data) or y+dy < 0 or x+dx >= len(data[0]) or x+dx < 0:
            break
        if data[y+dy][x+dx] == '#':
            dir = rotate[dir]
            dy, dx = get_offset[dir]
        
        y = y+dy
        x = x+dx
    
    visited = np.array(visited)
    return np.sum(visited)

def get_visited(data):
    y, x = find_start(data)
    dir = data[y][x]
    visited = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    while True:
        dy, dx = get_offset[dir] 
        visited[y][x] = 1
        if y+dy >= len(data) or y+dy < 0 or x+dx >= len(data[0]) or x+dx < 0:
            break
        if data[y+dy][x+dx] == '#':
            dir = rotate[dir]
            dy, dx = get_offset[dir]
        
        y = y+dy
        x = x+dx
    
    return visited



def printmap(data):
    for line in data:
        for c in line:
            print(c, end='')
        print()

import copy
# 1911
def part_2(data):
    vis = get_visited(data) 
    count = 0
    p_count = 0
    data = [list(s) for s in data]
    for i in range(len(data)):
        for j in range(len(data[0])):
            y, x = find_start(data)
            if (i == y and j == x) or (vis[i][j] == 0):
                continue
            data[i][j] = '#'
            
            dir = data[y][x]
            start = time.time()
            elapsedTime = 0
            while True:
                if elapsedTime > 0.02:
                    count += 1
                    data[i][j] = '.'
                    break

                dy, dx = get_offset[dir] 
                
                if y+dy >= len(data) or y+dy < 0 or x+dx >= len(data[0]) or x+dx < 0:
                    data[i][j] = '.'
                    break
                
                while data[y+dy][x+dx] == '#':
                    dir = rotate[dir]
                    dy, dx = get_offset[dir]
                 
                y = y+dy
                x = x+dx
                
                elapsedTime = time.time() - start
            p_count += 1 
    return count


input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 6), "s")
