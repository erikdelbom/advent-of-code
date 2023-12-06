import sys

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


def part_1(data):
    return None

def part_2(data):
    return None

input_file = sys.argv[1]

print("Part 1:", part_1(read_input(input_file)))
print("Part 2:", part_2(read_input(input_file)))