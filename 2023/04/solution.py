import re
import sys

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


def part_1(data):
    for line in data:
        numbers, winners = line.split(': ')[1].split(' | ')
        print(numbers, " - ",  winners)
        #numbers, winners = numbers.replace('  ', ' ').split(' '), winners.replace('  ', ' ').split(' ')
        
        #numbers, winners = set(map(int, numbers)), set(map(int, winners))


def part_2(data):
    return None

input_file = sys.argv[1]

print("Part 1:", part_1(read_input(input_file)))
print("Part 2:", part_2(read_input(input_file)))