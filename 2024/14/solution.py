import sys
import time

n = 103
m = 101
nmid = n // 2
mmid = m // 2

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def move_robot(pos, vel, sec):
    x = (pos[0] + vel[0]*sec) % m
    y = (pos[1] + vel[1]*sec) % n

    return x,y

def print_robots(robots):
    map = [[' ' for _ in range(m)] for _ in range(n)]
    for r in robots:
        p = r[0]
        map[p[1]][p[0]] = '#'

    for row in range(n):
        for col in range(m):
            print(map[row][col], end='')
        print()

def part_1(data):
    robots = []
    for line in data:
        p, v = line.split()
        p = eval(p.split('=')[1])
        v = eval(v.split('=')[1])   
        robots.append(move_robot(p, v, 100))
   
    robots = [r for r in robots if r[0] != mmid and r[1] != nmid]
    quad1 = [r for r in robots if r[0] < mmid and r[1] < nmid]
    quad2 = [r for r in robots if r[0] > mmid and r[1] < nmid]
    quad3 = [r for r in robots if r[0] < mmid and r[1] > nmid]
    quad4 = [r for r in robots if r[0] > mmid and r[1] > nmid]
    
    return len(quad1)*len(quad2)*len(quad3)*len(quad4)

def part_2(data):
    robots = []
    for line in data:
        p, v = line.split()
        p = eval(p.split('=')[1])
        v = eval(v.split('=')[1])   
        robots.append((p, v))
    
    sec = 0
    while True:
        print("Second:", sec)
        print_robots(robots)
        for i in range(len(robots)):
            p, v = robots[i]
            robots[i] = (move_robot(p, v, 1), v)
        input()
        sec += 1

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
