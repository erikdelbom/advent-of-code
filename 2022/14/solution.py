
def read_input():
    cave = [['.' for i in range(100000)] for i in range(600)]
    y_s = []
    with open('data.in', 'r') as f:
        for line in f:
            coords = list(map(str.strip, line.split(' -> ')))
            for i in range(len(coords)-1):
                x1, y1 = map(int, coords[i].split(','))
                x2, y2 = map(int, coords[i+1].split(','))
                y_s.append(y2)

                
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2)+1, 1):
                        cave[y][x1] = '#'
                elif y1 == y2:
                    for x in range(min(x1, x2), max(x1, x2)+1, 1):
                        cave[y1][x] = '#'
    return cave, max(y_s)

def drop_sand(cave):
    s_x = 500
    s_y = 0

    while cave[s_y+1][s_x] != '#' and cave[s_y+1][s_x] != 'o':
        s_y += 1

    if cave[s_y+1][s_x] == '#':
        cave[s_y][s_x] = 'o'
    
    elif cave[s_y+1][s_x] == 'o':
        placed = False
        while not placed:
            if s_y == 599:
                return False

            # Is below free?
            if cave[s_y+1][s_x] == '.':
                s_y += 1
                continue

            # Is left free?
            elif cave[s_y+1][s_x-1] == '.':
                s_y += 1
                s_x -= 1
                continue

            # Is right free?
            elif cave[s_y+1][s_x+1] == '.':
                s_y += 1
                s_x += 1
                continue
            
            # None free, place on top
            else:
                cave[s_y][s_x] = 'o'
                placed = True

    return True

def fill_sand(cave, max_y):
    s_x = 500
    s_y = 0

    if cave[s_y][s_x] == 'o':
        return False

    while cave[s_y+1][s_x] != '#' and cave[s_y+1][s_x] != 'o':
        s_y += 1

    if cave[s_y+1][s_x] == '#':
        cave[s_y][s_x] = 'o'
    
    elif cave[s_y+1][s_x] == 'o':
        placed = False
        while not placed:
            if s_y == max_y-1:
                cave[s_y][s_x] = 'o'
                placed = True

            # Is below free?
            if cave[s_y+1][s_x] == '.':
                s_y += 1
                continue

            # Is left free?
            elif cave[s_y+1][s_x-1] == '.':
                s_y += 1
                s_x -= 1
                continue

            # Is right free?
            elif cave[s_y+1][s_x+1] == '.':
                s_y += 1
                s_x += 1
                continue
            
            # None free, place on top
            else:
                cave[s_y][s_x] = 'o'
                placed = True

    return True

def part_1(data):
    cave = data[0]
    for i in range(1000):
        if not drop_sand(cave):
            return i

    return None


def part_2(data):
    cave = data[0]
    max_y = data[1] + 2

    count = 0
    while fill_sand(cave, max_y):
        count += 1

    # for i in range(14):
    #     print()
    #     print(i, end=' ')
    #     for j in range(450, 520, 1):
    #         print(cave[i][j], end='')
    # print()

    return count


print('Part 1:', part_1(read_input())) 
print('Part 2:', part_2(read_input())) 
