import sys

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def valid_coord(world, x, y):
    return (x < len(world[0])) and (x >= 0) and (y < len(world)) and (y >= 0)

def check_sign(world, x, y):
    return (not world[y][x].isnumeric()) and (world[y][x] != '.')

def check_gear(world, x, y):
    return world[y][x] == '*'


def valid(world, coords):
    valid_bool = False
    for x, y in coords:
        # NORTH
        if valid_coord(world, x, y-1):
            valid_bool = check_sign(world, x, y-1)
            if valid_bool: 
                break

        # NORTH EAST
        if valid_coord(world, x+1, y-1):
            valid_bool = check_sign(world, x+1, y-1)
            if valid_bool: 
                break
        # EAST
        if valid_coord(world, x+1, y):
            valid_bool = check_sign(world, x+1, y)
            if valid_bool: 
                break
        # SOUTH EAST
        if valid_coord(world, x+1, y+1):
            valid_bool = check_sign(world, x+1, y+1)
            if valid_bool: 
                break
        # SOUTH
        if valid_coord(world, x, y+1):
            valid_bool = check_sign(world, x, y+1)
            if valid_bool: 
                break
        # SOUTH WEST
        if valid_coord(world, x-1, y+1):
            valid_bool = check_sign(world, x-1, y+1)
            if valid_bool: 
                break
        # WEST
        if valid_coord(world, x-1, y):
            valid_bool = check_sign(world, x-1, y)
            if valid_bool: 
                break
        # NORTH WEST
        if valid_coord(world, x-1, y-1):
            valid_bool = check_sign(world, x-1, y-1)
            if valid_bool: 
                break
    
    return valid_bool

def add_gear(gears, coord, num):
    if coord not in gears.keys():
        gears[coord] = [num]
    else:
        gears[coord].append(num)

def find_gears(gears, world, coords, num):
    found = False
    for x, y in coords:
        # NORTH
        if valid_coord(world, x, y-1):
            if check_gear(world, x, y-1):
                add_gear(gears, (x, y-1), num)
                found = True

        # NORTH EAST
        if valid_coord(world, x+1, y-1):
            if check_gear(world, x+1, y-1):
                add_gear(gears, (x+1, y-1), num)
                found = True

        # EAST
        if valid_coord(world, x+1, y):
            if check_gear(world, x+1, y):
                add_gear(gears, (x+1, y), num)
                found = True

        # SOUTH EAST
        if valid_coord(world, x+1, y+1):
            if check_gear(world, x+1, y+1):
                add_gear(gears, (x+1, y+1), num)
                found = True

        # SOUTH
        if valid_coord(world, x, y+1):
            if check_gear(world, x, y+1):
                add_gear(gears, (x, y+1), num)
                found = True

        # SOUTH WEST
        if valid_coord(world, x-1, y+1):
            if check_gear(world, x-1, y+1):
                add_gear(gears, (x-1, y+1), num)
                found = True

        # WEST
        if valid_coord(world, x-1, y):
            if check_gear(world, x-1, y):
                add_gear(gears, (x-1, y), num)
                found = True

        # NORTH WEST
        if valid_coord(world, x-1, y-1):
            if check_gear(world, x-1, y-1):
                add_gear(gears, (x-1, y-1), num)      
                found = True

        if found: 
            return


def part_1(data):
    sum = 0
    for y, row in enumerate(data):
        iterator = enumerate(row)
        for x, x_val in iterator:
            if x_val.isnumeric():
                num = x_val
                coords = [(x, y)]
                if x < len(row)-1:
                    x, x_val = next(iterator)
                    while x_val.isnumeric():
                        num += x_val
                        coords.append((x, y))
                        if x < len(row)-1:
                            x, x_val = next(iterator)
                        else:
                            break
                if valid(data, coords):
                    sum += int(num)
    return sum


def part_2(data):
    sum = 0
    gears = {}
    for y, row in enumerate(data):
        iterator = enumerate(row)
        for x, x_val in iterator:
            if x_val.isnumeric():
                num = x_val
                coords = [(x, y)]
                if x < len(row)-1:
                    x, x_val = next(iterator)
                    while x_val.isnumeric():
                        num += x_val
                        coords.append((x, y))
                        if x < len(row)-1:
                            x, x_val = next(iterator)
                        else:
                            break
                
                find_gears(gears, data, coords, int(num))

    print(gears.items())
    for key, value in gears.items():
        if len(value) == 2:
            print(value)
            sum += value[0] * value[1]

    return sum

input_file = sys.argv[1]


print("Part 1:", part_1(read_input(input_file)))
print("Part 2:", part_2(read_input(input_file)))
