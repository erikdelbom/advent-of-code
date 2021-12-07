import sys

ROW_SIZE = 1000

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    x = 0
    y = 0

def parse_line(line, index):
    line = line.split(' -> ')[index].strip().split(',')
    x = int(line[0])
    y = int(line[1])
    c = Coordinate(x, y)

    return c

def print_map(vent_map):
    for i in range (ROW_SIZE):
        for j in range (ROW_SIZE):
            print(vent_map[j][i], end='')
        print()

vent_lines = []
vent_map = [[0] * ROW_SIZE for _ in range(ROW_SIZE)]


for line in sys.stdin:
    c1 = parse_line(line, 0)
    c2 = parse_line(line, 1)

    if c1.x == c2.x: 
        if c1.y < c2.y:
            for i in range(c1.y, c2.y+1, 1):
                vent_map[c1.x][i] += 1
        else:
            for i in range(c2.y, c1.y+1, 1):
                vent_map[c1.x][i] += 1
    elif c1.y == c2.y:
        if c1.x < c2.x:
            for i in range(c1.x, c2.x+1, 1):
                vent_map[i][c1.y] += 1
        else:
            for i in range(c2.x, c1.x+1, 1):
                vent_map[i][c1.y] += 1
    
sum = 0

for i in range(ROW_SIZE):
    for j in range(ROW_SIZE):
        if vent_map[i][j] > 1:
            sum += 1

print(sum)
