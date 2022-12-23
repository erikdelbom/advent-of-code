class Cost:
    def __init__(self, qty, type) -> None:
        self.qty = qty
        self.type = type

def read_input():
    blueprints = {}
    with open('test.in', 'r') as f:
        for line in f.readlines():
            blueprint_nr, rest = line.split(': ')
            blueprint_nr = int(blueprint_nr[-1])
            blueprints[blueprint_nr] = {}
            robots = list(map(str.strip, rest.split('Each ')))[1:]
            for robot in robots:
                costs = []
                type = robot.split()[0]
                qty = 0
                q_type = ''
                robot = robot.split()
                for i in range(len(robot)):
                    if robot[i].isdigit():
                        qty = int(robot[i])
                        q_type = robot[i+1].replace('.', '')
                        costs.append(Cost(qty, q_type))
                blueprints[blueprint_nr][type] = costs
    return blueprints

def search(blueprint):
    time_limit = 24
    robots = []
    # robot type, collected
    start_robot = ['ore', 0]
    robots.append(start_robot)

    paths = [robots]

    for minute in range(time_limit):
        for path in paths:
            pass
            # check for choices
            # make all choices and put in paths




def part_1(blueprints):
    for key, bp in blueprints.items():
        score = 0
        #search(blueprints[key])
        geode_cost = bp['geode']

print('Part 1:', part_1(read_input()))


