def read_input():
    with open('data.in', 'r') as f:
        pairs = []
        for line in f:
            if line != '\n':
                pairs.append(eval(line.strip()))
    return pairs

def compare_ints(left, right):
    if left < right: return True
    elif left > right: return False
    else: return None

def print_compares(left, right, res):
    print(left, '-', right)
    print('Result:', res)

def compare_lists(left, right):
    correct = None
    if type(left) == type(right):
        if isinstance(left, list):
            for i in range(len(left)):
                if correct == None:
                    if i == len(right):
                            return False
                    correct = compare_lists(left[i], right[i])
        elif isinstance(left, int):
            correct = compare_ints(left, right)
            print_compares(left, right, correct)
            return correct
    else:
        if isinstance(left, int):
            left = [left]
            correct = compare_lists(left, right)
            print_compares(left, right, correct)
            return correct
        elif isinstance(right, int):
            right = [right]
            correct = compare_lists(left, right)
            print_compares(left, right, correct)
            return correct
    # if correct == None:
    #     print_compares(left, right, True)
    #     return True
    print_compares(left, right, correct)
    return correct



def part_1(data):
    correct = []
    idx = 1
    for i in range(0, len(data), 2):
        left = data[i]
        right = data[i+1]
        ret = compare_lists(left, right)
        print("idx:", ret)
        print()
        if ret == True or ret == None:
            correct.append(idx)
        idx += 1
    
    return sum(correct)

print("Part 1:", part_1(read_input()))