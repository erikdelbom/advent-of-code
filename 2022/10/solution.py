def read_input():
    with open('data.in', 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def part_1(data):
    reg_x = 1
    cycle = 1
    vals = {}
    for line in data:
        if len(line.split()) == 2:
            op, arg = line.split()
            for i in range(2):
                vals[cycle] = cycle * reg_x
                cycle += 1 
            reg_x += int(arg)
        else:
            vals[cycle] = cycle * reg_x
            cycle += 1
    return vals[20] + vals[60] + vals[100] + vals[140] + vals[180] + vals[220]



def part_2(data):
    reg_x = 1
    cycle = 1
    result = '\n'
    cur_px = 0

    for line in data:
        if len(line.split()) == 2:
            op, arg = line.split()
            for i in range(2):
                if cur_px >= reg_x-1 and cur_px <= reg_x+1:
                    result += '#'
                else:
                    result += '.'
                cur_px += 1
                if cycle % 40 == 0:
                    cur_px = 0
                    result += '\n'
                cycle += 1 
            reg_x += int(arg)
        else:
            if cur_px >= reg_x-1 and cur_px <= reg_x+1:
                result += '#'
            else:
                result += '.'
            cur_px += 1
            
            if cycle % 40 == 0:
                result += '\n'
                cur_px = 0
            
            cycle += 1
    return result

print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))