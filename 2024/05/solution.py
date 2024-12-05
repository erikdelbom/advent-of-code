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

def sort(page, rules):
    sorted = [0 for _ in range(len(page))]
    counts = {}
    for p in page:
        count = 0 
        for c in page:
            if c in rules[p]:
                count += 1
        counts[p] = count
    
    for p in page:
        sorted[counts[p]] = p

    return sorted

def part_1(data):
    rules_in, pages = split_list(data, '')
    rules = {}
    for r in rules_in:
        a, b = map(int,r.split('|'))
        try:
            rules[a].append(b)
        except:
            rules[a] = [b]
   
    sum = 0
    for page in pages:
        valid = True
        page = list(map(int, page.split(',')))
        for i in range(len(page)-1):
            for j in range(i+1, len(page)):
                if page[j] not in rules[page[i]]:
                    valid = False
        if valid:
            sum += page[len(page)//2]

    return sum
   
def part_2(data):
    rules_in, pages = split_list(data, '')
    rules = {}
    for r in rules_in:
        a, b = map(int,r.split('|'))
        try:
            rules[a].append(b)
        except:
            rules[a] = [b]
   
    sum = 0
    for page in pages:
        valid = True
        page = list(map(int, page.split(',')))
        for i in range(len(page)-1):
            for j in range(i+1, len(page)):
                if page[j] not in rules[page[i]]:
                    valid = False
        if not valid:
            correct = sort(page, rules)
            sum += correct[len(page)//2]
                    
    return sum

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
