import sys
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def done(springs):
    for s in springs:
        if s == '?':
            return False
    return True

def valid(springs, sizes):
    continous = 0
    sizes_idx = 0
    result = []
    for i in range(springs):
        if springs[i] == '#':
            continuous += 1
        if springs[i] != '#':
            continous = 0
            if continous > sizes_idx:
                return False
    return True


def variations(springs, sizes):
    if done(springs):
        return springs

    for i in range(len(springs)):
        if springs[i] == '?':
            springs_copy = springs
            springs_copy[i] = '#'
            
            if valid(springs_copy, sizes):
                variations(springs_copy, sizes)

        



def part_1(data):
    result = 0   

    for line in data:
        springs, sizes = line.split()
        sizes = list(map(int, sizes.split(',')))
        

    return result

def part_2(data):
    return None

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")