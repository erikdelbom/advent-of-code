import sys
import time
import math

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


instr_lookup = { 'L': 0, 'R': 1 }

def get_instruction(instructions, instr_idx):
    instr = instructions[instr_idx]
    instr = instr_lookup[instr]
    instr_idx += 1
    if instr_idx == len(instructions):
        instr_idx = 0
    
    return instr, instr_idx

def part_1(data):
    route_table = {}

    instructions = data[0]
    data.pop(0)
    data.pop(0)

    for line in data:
        source, destinations = line.split(" = ")
        destination_l = destinations.split(", ")[0][1:]
        destination_r = destinations.split(", ")[1][:-1]
        route_table[source] = (destination_l, destination_r)

    steps = 0
    instr_idx = 0
    current = "AAA"
    while current != "ZZZ":
        steps += 1
        instr, instr_idx = get_instruction(instructions, instr_idx)
        current = route_table[current][instr]

    return steps

# Calculate steps for each cycle
# find lcm/gcd


def find_z(route_table, start, instructions):
    cycles = -1
    i = 0
    instr_idx = 0
    result = []
    current = start
    while i < 1:
        if current[2] == 'Z':
            result.append(cycles)
            result = cycles
            i += 1
        instr, instr_idx = get_instruction(instructions, instr_idx)
        current = route_table[current][instr]
        cycles += 1

    return cycles


def part_2(data):
    route_table = {}

    instructions = data[0]
    data.pop(0)
    data.pop(0)

    for line in data:
        source, destinations = line.split(" = ")
        destination_l = destinations.split(", ")[0][1:]
        destination_r = destinations.split(", ")[1][:-1]
        route_table[source] = (destination_l, destination_r)


    cycles = []
    for key in route_table.keys():
        if key[2] == 'A':
            cyc = find_z(route_table, key, instructions)
            cycles.append(cyc)

    print(cycles)
    lcm = math.lcm(*cycles)

    return lcm 



    print(cycles)

    # done = False
    # steps = 0
    # instr_idx = 0
    # while not done:
    #     for idx, cur in enumerate(current):
    #         if cur[2] != 'Z':
    #             break
        
    #         if idx == len(current)-1:
    #             done = True    

    #     steps += 1

    #     instr = instructions[instr_idx]
    #     instr = instr_lookup[instr]
    #     instr_idx += 1
    #     if instr_idx == len(instructions):
    #         instr_idx = 0

    #     new_current = []
    #     for cur in current:
    #         new_current.append(route_table[cur][instr])

    #     current = new_current

    #     # print(current)
    #     # print()
    #     # input()

    #return steps

input_file = sys.argv[1]

start_time = time.time()
#print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")