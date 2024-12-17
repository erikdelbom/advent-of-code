import sys
import time

offsets = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
lookaheads = {'^': 0, 'v': 0, '<': -2, '>': 2}

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def create_world(data):
    world = []
    for line in data:
        if line == '':
            break
        world.append(line)

    return list(map(list, world))

def create_wide_world(data):
    world = []
    for line in data:
        if line == '':
            break
        wide = []
        for c in line:
            if c == '@':
                wide.append(c)
                wide.append('.')
            elif c == 'O':
                wide.append('[')
                wide.append(']')
            else:
                wide.append(c)
                wide.append(c)
        world.append(wide)
    return world

def get_moves(data):
    capture = False
    moves = []
    for line in data:
        if line == '':
            capture = True
        if capture:
            moves.extend(line)
    return moves

def get_start(world):
    for row in range(len(world)):
        for col in range(len(world[0])):
            if world[row][col] == '@':
                return row, col

def move_boxes(world, pos, move):
    offy, offx = offsets[move]
    newy, newx = pos[0]+offy, pos[1]+offx
    trace = []

    while world[newy][newx] != '#':
        if world[newy][newx] == 'O':
            trace.append((newy, newx))
            newy, newx = newy+offy, newx+offx
        elif world[newy][newx] == '.':
            pos = '.'
            trace.append((newy, newx))
            for t in trace:
                world[t[0]][t[1]] = 'O'
            
            return True

    return False

def move_box(world, pos, move):
    if move == '<':
        world[pos[0]][pos[1]] = '.'
        world[pos[0]][pos[1]-1] = ']'
        world[pos[0]][pos[1]-2] = '['
    elif move == '>':
        world[pos[0]][pos[1]] = '.'
        world[pos[0]][pos[1]+1] = '['
        world[pos[0]][pos[1]+2] = ']'
    elif move == '^':
        world[pos[0]][pos[1]] = '.'
        world[pos[0]-1][pos[1]] = '['
        world[pos[0]][pos[1]+1] = '.'
        world[pos[0]-1][pos[1]+1] = ']'
    elif move == 'v':
        world[pos[0]][pos[1]] = '.'
        world[pos[0]+1][pos[1]] = '['
        world[pos[0]][pos[1]+1] = '.'
        world[pos[0]+1][pos[1]+1] = ']'

def move_wide_boxes(world, pos, move):
    if move == '<': 
        newy, newx = pos[0], pos[1]-2
        if world[newy][newx] == ']':
            if move_wide_boxes(world, (newy, newx), move):
                move_box(world, pos, move)
                return True
            else:
                return False
        elif world[newy][newx] == '.':
            move_box(world, pos, move)
            return True
        else:
            return False

    elif move == '>':
        newy, newx = pos[0], pos[1]+2
        if world[newy][newx] == '[':
            if move_wide_boxes(world, (newy, newx), move):
                move_box(world, pos, move)
                return True
            else:
                return False
        elif world[newy][newx] == '.':
            move_box(world, pos, move)
            return True
        else:
            return False       

    elif move == '^':
        left = False
        right = False
        y,x = pos
        if world[y][x] == ']':
            x = x-1
        
        if world[y-1][x] == ']':
            if move_wide_boxes(world, (y-1, x), move):
                move_box(world, (y, x), move)
                left = True 
            else:
                left = False
        elif world[y-1][x] == '[':
             if move_wide_boxes(world, (y-1, x), move):
                move_box(world, (y, x), move)
                left = True
                right = True
             else:
                left = False
                right = False
        
        print(left)
        if world[y-1][x+1] == '[' and left:
            if move_wide_boxes(world, (y-1,x+1), move):
                print("move")
                move_box(world, (y, x), move)
                return True
            else:
                return False
                                
        if world[y-1][x] == '.':
            move_box(world, (y, x), move)
            return True
        else:
            return False


    elif move == 'v':
        y,x = pos
        if world[y][x] == ']':
            x = x-1
        
        

def move(world, pos, move):
    offy,offx = offsets[move] 
    newy, newx = pos[0]+offy, pos[1]+offx
    
    if world[newy][newx] == '#':
        return pos
    
    elif world[newy][newx] == 'O':
        if move_boxes(world, (newy, newx), move):
            world[pos[0]][pos[1]] = '.'
            world[newy][newx] = '@'
            return newy, newx
        else:
            return pos
        
    elif world[newy][newx] == '.':
        world[pos[0]][pos[1]] = '.'
        world[newy][newx] = '@'
        return newy, newx

def wide_move(world, pos, move):
    offy,offx = offsets[move] 
    newy, newx = pos[0]+offy, pos[1]+offx
    
    if world[newy][newx] == '#':
        return pos
    
    elif world[newy][newx] == '[' or world[newy][newx] == ']':
        if move_wide_boxes(world, (newy, newx), move):
            world[pos[0]][pos[1]] = '.'
            world[newy][newx] = '@'
            return newy, newx
        else:
            return pos
        
    elif world[newy][newx] == '.':
        world[pos[0]][pos[1]] = '.'
        world[newy][newx] = '@'
        return newy, newx

def print_world(world):
    for i in range(len(world)):
        for j in range(len(world[0])):
            print(world[i][j], end='')
        print()

def sum_boxes(world):
    res = 0
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i][j] == 'O':
                res += i*100 + j
    return res

def part_1(data):
    world = create_world(data)
    moves = get_moves(data)
    pos = get_start(world)    

    for m in moves:
        pos = move(world, pos, m)

    return sum_boxes(world)    

def part_2(data):
    world = create_wide_world(data)
    moves = get_moves(data)
    pos = get_start(world)
    for m in moves:
        print_world(world)
        pos = wide_move(world, pos, m)

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
