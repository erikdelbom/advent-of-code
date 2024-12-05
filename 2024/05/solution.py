import sys
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def split_list(lst, delim):
    result = []
    current = []
    for item in lst:
        if item == delim:
            if current:
                result.append(current)
                current = []
        else:
            current.append(item)
    if current:
        result.append(current)
    return result

def sort_rules(rules):
    sorted = []
    for a in rules.keys():
        for r in rules[a]:
            

def part_1(data):
    rules_in, pages = split_list(data, '')
    rules = {}
    for r in rules_in:
        a, b = map(int,r.split('|'))
        try:
            rules[a].append(b)
        except:
            rules[a] = [b]

    for key in rules.keys():
        print(key, rules[key])
   
def part_2(data):
    return None

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
