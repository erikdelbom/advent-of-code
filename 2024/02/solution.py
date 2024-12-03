import sys
import time
import numpy as np

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def valid(report):
    valid = 1
    prev_diff = report[0] - report[1]
    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        if not (prev_diff * diff > 0 and abs(diff) < 4):
            valid = 0
            break
    return valid

def sub_reports(report):
    return [report[:i] + report[i+1:] 
           for i in range(len(report))]

def part_1(data):
    count = 0
    for report in data: 
        report = list(map(int, report.split()))
        count += valid(report)
    return count 

def part_2(data):
    count = 0
    for report in data: 
        report = list(map(int, report.split()))
        if valid(report) == 0:
            subs = sub_reports(report)
            for sub in subs:
                if valid(sub) == 1:
                    count += 1
                    break
        else:
            count += 1
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
