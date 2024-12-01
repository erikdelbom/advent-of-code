import sys
import time
import numpy as np

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def part_1(data):
    left = []
    right = []
    for line in data:
        if line:
            l, r = list(map(int, line.split()))
            left.append(l)
            right.append(r)
    left = np.array(left)
    right = np.array(right)
    left = np.sort(left)
    right = np.sort(right)

    return np.sum(np.abs(left - right))

def part_2(data):
    left = []
    right = []
    for line in data:
        if line:
            l, r = list(map(int, line.split()))
            left.append(l)
            right.append(r)
    left = np.array(left)
    right = np.array(right)
    left = np.sort(left)
    right = np.sort(right)
    
    sum = 0
    for l in left:
        count = (right == l).sum()
        sum += l*count

    return sum

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
