import sys
import time
import numpy as np

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def valid(diff, deriv, i):
    if not (abs(diff) > 0 and abs(diff) < 4):
        return False

    if deriv


def part_1(data):
    count = 0
    for report in data: 
        report = np.array(list(map(int, report.split())))
        roll = np.roll(report, -1)[:-1]
        diffs = report[:-1] - roll
        
        neg = np.sum(diffs < 0)
        pos = np.sum(diffs > 0)

        if not (neg == len(diffs) or pos == len(diffs)):
            continue

        if np.all(np.abs(diffs) <= 3):
            count += 1

    return count 

def part_2(data):
    count = 0
    for report in data: 
        report = list(map(int, report.split()))
        deriv = 0
        for i in range(len(report)-1):
            diff = report[i] - report[i-1]
            
            d = 0
            if diff != 0:
                d = 1 if abs(diff) == diff else -1
            deriv += d

            if not (deriv == i or deriv == -i):
                break

            if abs(diff)
            



    return count 

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")


# 7 6 4 2 1
# 6 2 2 1
# 1 4 2 1

#  1  3  2  4  5
#  3  2  4  5
# -1  1 -2 -1
