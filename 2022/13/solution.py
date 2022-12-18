def read_input():
    with open('test.in', 'r') as f:
        pairs = []
        for line in f:
            if line != '\n':
                pairs.append(eval(line.strip()))
    return pairs

def compare(left, right):
    if type(right) == type(left):
        if isinstance(right, list) and isinstance(left, list):
            print("comparing lists")
            for i in range(len(right)):
                if i == len(left): return False
                ret = compare(left[i], right[i])
                if ret:
                    return True
        elif isinstance(right, int) and isinstance(left, int):
            print("comparing ints", left, right)
            if left < right:
                return True
            else:
                return False
    else:
        print("not same", left, right)
        if isinstance(right, int):
            right = [right]
            if not compare(left, right):
                return False
        elif isinstance(left, int):
            left = [left]
            if not compare(left, right):
                return False

    return True

def part_1(data):
    count = []
    idx = 1
    for i in range(0, len(data)-1, 2):
        left = data[i]
        right = data[i+1]
        print(left, "-", right)
        if compare(left, right):
            count.append(idx)
        idx += 1
        print('-----------------------------')
        
    return count#sum(count)
        
        

print("Part 1:", part_1(read_input()))