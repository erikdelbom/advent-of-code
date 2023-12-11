import sys
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def empty_column(image, x):
    for y in range(len(image)):
        if image[y][x] != '.':
            return False
    return True

def empty_row(image, y):
    for x in range(len(image[y])):
        if image[y][x] != '.':
            return False
    return True

def insert_column(image, x):
    for y in range(len(image)):
        image[y].insert(x+1, '.')

def insert_row(image, y):
   row = ['.' for i in range(len(image[y]))]
   image.insert(y+1, row)

def expand(image):
    empty_rows = []
    for y in range(len(image)):
        if empty_row(image, y):
            empty_rows.append(y)

    empty_cols = []
    for x in range(len(image[0])):
        if empty_column(image, x):
            empty_cols.append(x)

    for y in empty_rows:
        insert_row(image, y)

    for x in empty_cols:
        insert_column(image, x)

def convert(image):
    for i in range(len(image)):
        image[i] = list(image[i])

def print_image(image):
    for row in image:
        for col in row:
            print(col, end='')
        print()

def 

def part_1(data):
    print_image(data)
    convert(data)
    expand(data)
    print()
    print_image(data)

def part_2(data):
    return None

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")