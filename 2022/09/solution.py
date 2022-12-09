def read_input():
    with open('test.in', 'r') as f:
        lines = list(map(str.rstrip, f.readlines()))
        p = []
        for l in lines:
            tmp = l.split()
            tmp[1] = int(tmp[1])
            p.append(tmp)
        return p

def part_1(data):
    locations = {  }
    h_x = 0
    h_y = 0
    t_x = 0
    t_y = 0

    if data[0][0] == 'U':
        h_y += 1
    if data[0][0] == 'R':
        h_x += 1
    if data[0][0] == 'D':
        h_y -= 1
    if data[0][0] == 'L':
        h_x -= 1

    for line in data:
        print(line)
        dir = line[0]
        steps = line[1]
        if dir == 'U':
            for i in range(steps):
                if h_x == t_x:
                    h_y += 1
                    t_y += 1
                    locations[(t_x, t_y)] = 1 if (t_x, t_y) not in locations else locations[(t_x, t_y)] + 1
                elif h_y == t_y:
                    h_y += 1
                elif h_x != t_x and h_y != t_y:
                    h_y += 1
                    t_x = h_x
                    t_y = h_y - 1
                    locations[(t_x, t_y)] = 1 if (t_x, t_y) not in locations else locations[(t_x, t_y)] + 1

        elif dir == 'R':
            for i in range(steps):
                if h_y == t_y:
                    h_x += 1
                    t_x += 1
                    locations[(t_x, t_y)] = 1 if (t_x, t_y) not in locations else locations[(t_x, t_y)] + 1
                elif h_x == t_x:
                    h_x += 1
                elif h_x != t_x and h_y != t_y:
                    h_x += 1
                    t_y = h_y
                    t_x = h_x - 1
                    locations[(t_x, t_y)] = 1 if (t_x, t_y) not in locations else locations[(t_x, t_y)] + 1
        
        elif dir == 'D':
            for i in range(steps):
                if h_x == t_x:
                    h_y -= 1
                    t_y -= 1
                    locations[(t_x, t_y)] = 1 if (t_x, t_y) not in locations else locations[(t_x, t_y)] + 1
                elif h_y == t_y:
                    h_y -= 1
                elif h_x != t_x and h_y != t_y:
                    h_y -= 1
                    t_x = h_x
                    t_y = h_y + 1
                    locations[(t_x, t_y)] = 1 if (t_x, t_y) not in locations else locations[(t_x, t_y)] + 1
        
        elif dir == 'L':
            for i in range(steps):
                if h_y == t_y:
                    h_x -= 1
                    t_x -= 1
                    locations[(t_x, t_y)] = 1 if (t_x, t_y) not in locations else locations[(t_x, t_y)] + 1
                elif h_x == t_x:
                    h_x -= 1
                elif h_x != t_x and h_y != t_y:
                    h_x -= 1
                    t_y = h_y
                    t_x = h_x + 1
                    locations[(t_x, t_y)] = 1 if (t_x, t_y) not in locations else locations[(t_x, t_y)] + 1
        print(t_x, t_y, h_x, h_y)
    return len(locations)
        

def part_2(data):
    pass
print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))