from functools import cmp_to_key

def read_input():
    with open('data.in', 'r') as f:
        lines = list(map(str.strip, f.readlines()))
        data = []
        for l in lines:
            if l != '':
                data.append(eval(l))
        return data

def compare(left, right):
    result = None
    # Both are lists
    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if result == None:
                if i == len(right): return False
                result = compare(left[i], right[i])
        if result == None and len(left) < len(right): return True
    
    # Both are ints
    elif isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None

    # Left is int, right is list
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        return compare(left, right)

    # Left is list, right is int
    elif isinstance(left, list) and isinstance(right, int):
        right = [right]
        return compare(left, right)

    return result

def comp(left, right):
    if compare(left,right): return -1
    elif not compare(left,right): return 1

def part_1(data):
    correct = []
    idx = 1
    for i in range(0, len(data), 2):
        left = data[i]
        right = data[i+1]
        result = None
        ret = compare(left, right)
        if ret == True or ret == None:
            correct.append(idx) 
        idx += 1

    return sum(correct)

def part_2(data):
    data.append([[2]])
    data.append([[6]])

    data = sorted(data, key=cmp_to_key(comp))
    result = 1
    for idx, d in enumerate(data):
        if d == [[2]] or d == [[6]]:
            result *= (idx+1)
    return(result)


print('Part 1:', part_1(read_input())) 
print('Part 2:', part_2(read_input())) 

