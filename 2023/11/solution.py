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

def insert_column(image, x, cols):
    for y in range(len(image)):
        image[y].insert(x, '.')
    for i in range(len(cols)):
        cols[i] += 1

def insert_row(image, y, rows):
    row = ['.' for i in range(len(image[y]))]
    image.insert(y, row)
    for i in range(len(rows)):
        rows[i] += 1

def convert(image):
    for i in range(len(image)):
        image[i] = list(image[i])

def print_image(image):
    for row in image:
        for col in row:
            print(col, end='')
        print()


def find_galaxies(image):
    result = []
    for y in range(len(image)):
        for x in range(len(image[y])):
            if image[y][x] == '#':
                result.append([x, y])
    return result

def manhattan(start, end):
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

def find_galaxies_fast(image, times):
    empty_rows = []
    for y in range(len(image)):
        if empty_row(image, y):
            empty_rows.append(y)

    empty_cols = []
    for x in range(len(image[0])):
        if empty_column(image, x):
            empty_cols.append(x)

    galaxies = find_galaxies(image)

    for i in range(len(galaxies)):
        gal_x, gal_y = galaxies[i]
        for col in empty_cols:
            if col < gal_x:
                galaxies[i][0] += times-1
        for row in empty_rows:
            if row < gal_y:
                galaxies[i][1] += times-1

    new_galaxies = []
    for galaxy in galaxies:
        new_galaxies.append((galaxy[0], galaxy[1]))

    return new_galaxies


def part_1(data):
    convert(data)
    galaxies = find_galaxies_fast(data, 2)

    galaxies_dist = {}

    for start in galaxies:
        distances = {}
        for end in galaxies:
            if start == end:
                continue
            distances[end] = manhattan(start, end)
        galaxies_dist[start] = distances
    
    removed = []
    sum = 0
    for key in galaxies_dist.keys():
        for galaxy in galaxies_dist[key].keys():
            if galaxy not in removed:
                sum += galaxies_dist[key][galaxy]
        removed.append(key)

    return sum

def part_2(data):
    convert(data)
    galaxies = find_galaxies_fast(data,1_000_000)

    galaxies_dist = {}

    for start in galaxies:
        distances = {}
        for end in galaxies:
            if start == end:
                continue
            distances[end] = manhattan(start, end)
        galaxies_dist[start] = distances
    
    removed = []
    sum = 0
    for key in galaxies_dist.keys():
        for galaxy in galaxies_dist[key].keys():
            if galaxy not in removed:
                sum += galaxies_dist[key][galaxy]
        removed.append(key)

    return sum

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")