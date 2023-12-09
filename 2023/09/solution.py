import sys
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def get_difference(numbers):
    result = []
    for i in range(len(numbers)-1):
        src = numbers[i]
        dest = numbers[i+1]
        result.append(dest-src)
    return result

def zero(numbers):
    for n in numbers:
        if n != 0:
            return False
    return True


def search(stages, numbers):
    stages.append(numbers)
    if zero(numbers):
        return numbers
    
    difference = get_difference(numbers)

    return search(stages, difference)


def extrapolate(stages):
    for i in range(len(stages)-1, 0, -1):
        if i == len(stages)-1:
            stages[i].append(0)
        else:
            extrap = stages[i-1][-1] + stages[i][-1]
            stages[i-1].append(extrap)

    return stages

def extrapolate_backwards(stages):
    for i in range(len(stages)-1, 0, -1):
        if i == len(stages)-1:
            stages[i].append(0)
        else:
            extrap = stages[i-1][0] - stages[i][0]
            stages[i-1].insert(0, extrap)

    return stages


def part_1(data):
    sum = 0
    for line in data:
        numbers = list(map(int, line.split()))
        diff = get_difference(numbers)
        stages = []
        search(stages, numbers)
        extrapolate(stages)
        sum += stages[0][-1]

    return sum

def part_2(data):
    sum = 0
    for line in data:
        numbers = list(map(int, line.split()))
        diff = get_difference(numbers)
        stages = []
        search(stages, numbers)
        extrapolate_backwards(stages)
        sum += stages[0][0]

    return sum

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")