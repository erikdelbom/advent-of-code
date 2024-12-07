import sys
import time
import numpy as np
from itertools import product

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def parse_line(line):
    result, terms = line.split(": ")
    result = int(result)
    terms = list(map(int, terms.split()))
    
    return result, np.array(terms)

def part_1(data):
    count = 0
    for line in data:
        result, terms = parse_line(line)
        perms = [''.join(p) for p in product(['+', '*'], repeat=len(terms)-1)]
        stop = False
        for perm in perms:
            if stop:
                break
            sum = terms[0]
            opidx = 0
            for i in range(1, len(terms)):
                op = perm[opidx]
                opidx += 1
                if op == '+':
                    sum += terms[i]
                else:
                    sum *= terms[i]
            if sum == result:
                count += result
                stop = True

    return count

def part_2(data):
    count = 0
    for line in data:
        result, terms = parse_line(line)
        perms = [''.join(p) for p in product(['+', '*', '|'], repeat=len(terms)-1)]
        stop = False
        for perm in perms:
            if stop:
                break
            sum = terms[0]
            opidx = 0
            for i in range(1, len(terms)):
                op = perm[opidx]
                opidx += 1
                if op == '+':
                    sum += terms[i]
                elif op == '*':
                    sum *= terms[i]
                else:
                    tmp = str(sum) + str(terms[i])
                    sum = int(tmp)
            if sum == result:
                count += result
                stop = True

    return count


input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
