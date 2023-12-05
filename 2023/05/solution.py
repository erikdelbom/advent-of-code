import sys

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


def part_1(data):
    parts = []
    part = []
    for line in data:
        if line == '':
            parts.append(part)
            part = []
        else:
            part.append(line)
    seeds = list(map(int, parts[0][0].split(': ')[1].split()))

    map_dict = {}    

    for part in parts:
        key = part[0].split(' map:')[0]
        part.pop(0)
        for subpart in part:
            print(subpart)


    
    

def part_2(data):
    return None

input_file = sys.argv[1]

print("Part 1:", part_1(read_input(input_file)))
print("Part 2:", part_2(read_input(input_file)))