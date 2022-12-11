from math import sqrt

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def read_input():
    with open('data.in', 'r') as f:
        lines = list(map(str.rstrip, f.readlines()))
        p = []
        for l in lines:
            tmp = l.split()
            tmp[1] = int(tmp[1])
            p.append(tmp)
        return p

def euclidean_distance(p1, p2):
    return sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2)

def get_direction(p1, p2):
    if p1.x == p2.x and p1.y < p2.y:
        return 'N'
    elif p1.x < p2.x and p1.y < p2.y:
        return 'NE'
    elif p1.x < p2.x and p1.y == p2.y:
        return 'E'
    elif p1.x < p2.x and p1.y > p2.y:
        return 'SE'
    elif p1.x == p2.x and p1.y > p2.y:
        return 'S'
    elif p1.x > p2.x and p1.y > p2.y:
        return 'SW'
    elif p1.x > p2.x and p1.y == p2.y:
        return 'W'
    elif p1.x > p2.x and p1.y < p2.y:
        return 'NW'


def move_knots(knots):
    for i in range(1, len(knots)):
        if euclidean_distance(knots[i], knots[i-1]) >= 2:
            dir = get_direction(knots[i], knots[i-1])

            if dir == 'N':
                knots[i].y += 1
            elif dir == 'NE':
                knots[i].x += 1
                knots[i].y += 1
            elif dir == 'E':
                knots[i].x += 1
            elif dir == 'SE':
                knots[i].x += 1
                knots[i].y -= 1
            elif dir == 'S':
                knots[i].y -= 1
            elif dir == 'SW':
                knots[i].x -= 1
                knots[i].y -= 1
            elif dir == 'W':
                knots[i].x -= 1
            elif dir == 'NW':
                knots[i].x -= 1
                knots[i].y += 1
        


def move_rope(data, size):
    locations = {}
    knots = [Coord(0, 0) for i in range(size)]  

    for line in data:
        dir = line[0]
        steps = line[1] 

        if dir == 'U':
            for i in range(steps):
                knots[0].y += 1
                move_knots(knots)
                locations[(knots[-1].x, knots[-1].y)] = 1

        elif dir == 'R':
            for i in range(steps):
                knots[0].x += 1
                move_knots(knots)
                locations[(knots[-1].x, knots[-1].y)] = 1

        elif dir == 'D':
            for i in range(steps):
                knots[0].y -= 1
                move_knots(knots)
                locations[(knots[-1].x, knots[-1].y)] = 1

        elif dir == 'L':
            for i in range(steps):
                knots[0].x -= 1
                move_knots(knots)
                locations[(knots[-1].x, knots[-1].y)] = 1

    return len(locations)

def part_1(data):
    return move_rope(data, 2)

def part_2(data):
    return move_rope(data, 10)


print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))