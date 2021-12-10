import sys
import math

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
            if vent_map[j][i] == 0:
                print('.', end='')
            else:
                print(vent_map[j][i], end='')
        print()

def angle(c1, c2):
    delta_x = c2.x - c1.x
    delta_y = c2.y - c1.y

    if math.degrees(math.atan2(delta_y, delta_x)) % 45 == 0:
        if math.degrees(math.atan2(delta_y, delta_x)) % 90 != 0:
            return 45;
        else:
            return 0;

    return math.degrees(math.atan2(delta_y, delta_x))

vent_lines = []
vent_map = [[0] * ROW_SIZE for _ in range(ROW_SIZE)]


for line in sys.stdin:
    c1 = parse_line(line, 0)
    c2 = parse_line(line, 1)

    if angle(c1, c2) == 0:
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
   
    elif angle(c1, c2) == 45:
        if c1.x < c2.x:
            if c1.y < c2.y:
                y = c1.y
                for i in range(c1.x, c2.x+1):
                    vent_map[i][y] += 1
                    y += 1
            elif c1.y > c2.y:
                y = c1.y
                for i in range(c1.x, c2.x+1):
                    vent_map[i][y] += 1
                    y -= 1
        elif c1.x > c2.x:
            if c1.y < c2.y:
                y = c2.y
                for i in range(c2.x, c1.x+1):
                    vent_map[i][y] += 1
                    y -= 1
            elif c1.y > c2.y:
                y = c2.y
                for i in range(c2.x, c1.x+1):
                    vent_map[i][y] += 1
                    y += 1
   
sum = 0

for i in range(ROW_SIZE):
    for j in range(ROW_SIZE):
        if vent_map[i][j] > 1:
            sum += 1

print(sum)

