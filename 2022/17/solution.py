def read_input():
    with open('data.in', 'r') as f:
        return f.readline()

walls = (0, 8)
shapes = [
    ((3, 0), (4, 0), (5, 0), (6, 0)), 
    ((3, 1), (4, 0), (4, 1), (4, 2), (5, 1)), 
    ((3, 0), (4, 0), (5, 0), (5, 1), (5, 2)), 
    ((3, 0), (3, 1), (3, 2), (3, 3)), 
    ((3, 0), (3, 1), (4, 0), (4, 1))
]

directions = { '<' : -1, '>' : 1}

def spawn_rock(shape, start):
    rock = []
    for block in shape:
        x = block[0]
        y = start + block[1] 
        new_block = [x, y]
        rock.append(new_block)
    return rock

def vertical_collision(placed_rocks, falling_rock):
    for rock in placed_rocks:
        for block in rock:
            for falling_block in falling_rock:
                if block[0] == falling_block[0] and block[1]+1 == falling_block[1]:
                    #print('hit')
                    return True
    return False

def horizontal_collision(placed_rocks, falling_rock, direction):
    wall = 1 if direction == -1 else 7
    for block in falling_rock:
        if block[0] == wall:
            return True
    
    for rock in placed_rocks:
        for block in rock:
            for falling_block in falling_rock:
                if block[1] == falling_block[1] and block[0] == falling_block[0]+direction:
                    return True
    return False

def move_down(rock):
    for block in rock:
        block[1] -= 1

def move_sideways(rock, direction):
    for block in rock:
        block[0] += direction

def hit_floor(rock):
    for block in rock:
        if block[1] == 1:
            return True
    return False

def top_block(rock):
    return sorted(rock, key=lambda x: x[1], reverse=True)[0][1]

def hit_wall(rock, direction):
    limit = 1 if direction == -1 else 7
    for block in rock:
        if block[0] == limit:
            return True
    return False



def part_1(winds):
    start = 5
    shape_idx = 0
    wind_idx = 0
    placed_rocks = []
    current_height = 0
    # for shape in shapes:
    #     grid = [['.' for i in range(8)] for i in range(10)]
    #     rock = spawn_rock(shape, start)
    #     for block in rock:
    #         x = block[0]
    #         y = block[1]
    #         grid[y][x] = '@'
    #     for row in range(9, -1, -1):
    #         print()
    #         for col in range(8):
    #             print(grid[row][col], end='')
    #     print()

    for tick in range(2022):
        shape = shapes[shape_idx]
        rock = spawn_rock(shape, start)
        #print('Before falling:', rock)
        while not vertical_collision(placed_rocks, rock):
            if hit_floor(rock):
                break
            
            wind = winds[wind_idx]
            #print(wind)
            direction = directions[wind]

            move_down(rock)
            if not horizontal_collision(placed_rocks, rock, direction):
                move_sideways(rock, direction)
            #print(rock)
            wind_idx = (wind_idx + 1) % len(winds)

        #print('After falling:', rock)
        #print(top_block(rock))
        #input()
        current_height = max(top_block(rock), current_height)
        placed_rocks.append(rock)
        shape_idx = (shape_idx + 1) % 5
        start = current_height + 5
    
    return current_height



print('Part 1:', part_1(read_input()))