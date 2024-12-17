import sys
import time
import re

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def solve_diophantine(a, b, c):
    gcd, x0, y0 = extended_gcd(a, b)
    if c % gcd != 0:
        return (None, None, None)
    scale = c // gcd
    return x0 * scale, y0 * scale, gcd


def solve_system(ax, bx, cx, ay, by, cy):
    x1, x2, gcdx = solve_diophantine(ax, bx, cx)
    if x1 is None:
        return 0, 0
    ax1 = bx // gcdx
    bx1 = -ax // gcdx

    y_new = ay * ax1 + by * bx1
    cy_new = cy - ay * x1 - by * x2

    t = cy_new // y_new
    if cy_new % y_new != 0:
        return 0, 0

    x = x1 + t * ax1
    y = x2 + t * bx1

    return x, y

def part_1(data):
    res = 0
    for i in range(0, len(data), 4):
        ax = int(re.search(r"X\+[0-9]+", data[i]).group().split('+')[1])
        ay = int(re.search(r"Y\+[0-9]+", data[i]).group().split('+')[1])
        bx = int(re.search(r"X\+[0-9]+", data[i+1]).group().split('+')[1])
        by = int(re.search(r"Y\+[0-9]+", data[i+1]).group().split('+')[1])
        cx = int(re.search(r"X\=[0-9]+", data[i+2]).group().split('=')[1])
        cy = int(re.search(r"Y\=[0-9]+", data[i+2]).group().split('=')[1])
        
        x, y = solve_system(ax, bx, cx, ay, by, cy)
        res += 3*x + y
    return res

def part_2(data):
    res = 0
    for i in range(0, len(data), 4):
        ax = int(re.search(r"X\+[0-9]+", data[i]).group().split('+')[1])
        ay = int(re.search(r"Y\+[0-9]+", data[i]).group().split('+')[1])
        bx = int(re.search(r"X\+[0-9]+", data[i+1]).group().split('+')[1])
        by = int(re.search(r"Y\+[0-9]+", data[i+1]).group().split('+')[1])
        cx = int(re.search(r"X\=[0-9]+", data[i+2]).group().split('=')[1])
        cy = int(re.search(r"Y\=[0-9]+", data[i+2]).group().split('=')[1])
        
        x, y = solve_system(ax, bx, cx+10000000000000, ay, by, cy+10000000000000)
        res += 3*x + y
    return res

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
