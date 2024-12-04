import sys
import time
import re

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def neg_diagonals(data):
    row_start = len(data)-1
    diagonals = []
    for row in range(row_start, -1, -1):
        diag = ""
        col = 0
        while row < len(data):
            diag += data[row][col]
            row += 1
            col += 1
        diagonals.append(diag)
    
    col_stop = len(data[0])
    for col in range(1, col_stop):
        diag = ""
        row = 0
        while col < len(data[0]):
            diag += data[row][col]
            row += 1
            col += 1
        diagonals.append(diag)

    return diagonals

def pos_diagonals(data):
    row_start = len(data)-1
    diagonals = []
    for row in range(row_start, 0, -1):
        diag = ""
        col = len(data[0])-1
        while row < len(data):
            diag += data[row][col]
            row += 1
            col -= 1
        diagonals.append(diag)
    
    col_start = len(data[0])-1
    col_stop = 2
    for col in range(col_start, col_stop, -1):
        diag = ""
        row = 0
        while col >= 0:
            diag += data[row][col]
            row += 1
            col -= 1
        diagonals.append(diag)

    return diagonals

def part_1(data):
    count = 0
    regex = "(?=(XMAS|SAMX))"
    # row wise
    for line in data:
        matches = re.findall(regex, line)
        count += len(matches)
    # col wise
    for col in range(len(data[0])):
        line = "".join([row[col] for row in data])
        matches = re.findall(regex, line)
        count += len(matches)

    # negative diagnonals
    diagonals = neg_diagonals(data)
    for line in diagonals:
        matches = re.findall(regex, line)
        count += len(matches)

    # positive diagonals
    diagonals = pos_diagonals(data) 
    for line in diagonals:
        matches = re.findall(regex, line)
        count += len(matches)

    return count

def xmas(data, row, col):
    if data[row][col] == 'A':
        nw = data[row-1][col-1]
        ne = data[row-1][col+1]
        se = data[row+1][col+1]
        sw = data[row+1][col-1]
        
        diag1 = nw + 'A' + se 
        diag2 = ne + 'A' + sw

        if (diag1 == 'SAM' or diag1 == 'MAS') and (diag2 == 'SAM' or diag2 == 'MAS'):
            return True
    return False

        

def part_2(data):
    count = 0
    for row in range(1, len(data)-1):
        for col in range(1, len(data[0])-1):
            if xmas(data, row, col):
                count += 1
    return count

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
