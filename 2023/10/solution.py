import sys
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)

valid_pipes = { "north": ['|', '7', 'F'], 
                "east":  ['-', '7', 'J'],
                "south": ['|', 'L', 'J'],
                "west":  ['-', 'L', 'F'] }

next_dir_lookup = { "north7": "west", "northF": "east",
                    "east7": "south", "eastJ": "north",
                    "southL": "east", "southJ": "west",
                    "westL": "north", "westF": "south"}

offsets = { "north": (0, -1), "east": (1, 0),
            "south": (0, 1), "west": (-1, 0) }

class Agent:
    def __init__(self, start_x, start_y, start_dir):
        self.x = start_x
        self.y = start_y
        self.steps = 0
        self.dir = start_dir


def valid_coord(pipe_map, x, y):
    x_min, x_max = 0, len(pipe_map[0])
    y_min, y_max = 0, len(pipe_map)

    return (x >= x_min and x < x_max) and (y >= y_min and y < y_max)


def peek(pipe_map, x, y, dir):
    x_off, y_off = dir
    peek_x, peek_y = x+x_off, y+y_off
    if valid_coord(pipe_map, peek_x, peek_y):
        return pipe_map[y+y_off][x+x_off]
    return '.'


def peek_all(pipe_map, x, y):
    result = {}
    result["north"] = peek(pipe_map, x, y, NORTH)
    result["east"] = peek(pipe_map, x, y, EAST)
    result["south"] = peek(pipe_map, x, y, SOUTH)
    result["west"] = peek(pipe_map, x, y, WEST)

    return result


def find_start(pipe_map):
    for row_idx, row in enumerate(pipe_map):
        for col_idx, col in enumerate(row):
            if col == 'S':
                return col_idx, row_idx


def find_next_pipes(pipe_map, x, y):
    result = []
    peeks = peek_all(pipe_map, x, y)
    for key in peeks.keys():
        if peeks[key] in valid_pipes[key]:
            result.append((key, peeks[key]))
    return result


def next_dir(current_dir, next_sign):
    if current_dir+next_sign in next_dir_lookup.keys():
        return next_dir_lookup[current_dir+next_sign]
    return current_dir

def next_pos(agent, next_direction, next_sign):
    x_off, y_off = offsets[next_direction]
    agent.x = agent.x + x_off
    agent.y = agent.y + y_off

def move_agent(agent, pipe_map):
    next_pipes = find_next_pipes(pipe_map, agent.x, agent.y)
    for pipe in next_pipes:
        if pipe[0] == agent.dir:
            next_direction, next_sign = pipe

    agent.dir = next_dir(agent.dir, next_sign)
    next_pos(agent, next_direction, next_sign)
    agent.steps += 1


def count_trapped(loop_map):
    pass


def part_1(data):
    start_x, start_y = find_start(data)
    start_directions = find_next_pipes(data, start_x, start_y)
    agents = []
    for dir, sign in start_directions:
        agent_tmp = Agent(start_x, start_y, dir)
        next_pos(agent_tmp, dir, sign)
        agent_tmp.dir = next_dir(dir, sign)
        agent_tmp.steps += 1
        agents.append(agent_tmp)

    while True:
        for agent in agents:
            move_agent(agent, data)
         
        if agents[0].x == agents[1].x and agents[0].y == agents[1].y:
            return agents[0].steps

def part_2(data):
    loop_map = [['.' for x in range(len(data[0]))] for y in range(len(data))]
    start_x, start_y = find_start(data)
    loop_map[start_y][start_x] = 'X'
    start_directions = find_next_pipes(data, start_x, start_y)
    agents = []
    for dir, sign in start_directions:
        agent_tmp = Agent(start_x, start_y, dir)
        next_pos(agent_tmp, dir, sign)
        agent_tmp.dir = next_dir(dir, sign)
        agent_tmp.steps += 1
        agents.append(agent_tmp)

    while True:
        for agent in agents:
            loop_map[agent.y][agent.x] = 'X'
            move_agent(agent, data)
        

        if agents[0].x == agents[1].x and agents[0].y == agents[1].y:
            break

    return count_trapped(loop_map)
    


input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")