class Valve:
    def __init__(self, name, fr) -> None:
        self.name = name
        self.flow_rate = fr
        self.neighbors = []
        self.open = False
        self.steps = -1

    def add_neighbour(self, n):
        self.neighbors.append(n)

    def print(self):
        print('Name:', self.name)
        print('Flow rate:', self.flow_rate)
        print('Open:', self.open)

def read_input():
    valves = {}
    with open('test.in', 'r') as f:
        for line in f:
            valve_info, neighbor_info = line.split(';')
            name = valve_info.split()[1]
            fr = int(valve_info.split('=')[1])
            tmp = Valve(name, fr)
            neighbors = neighbor_info.split('valve')[1].split()
            for n in neighbors:
                if n != 's':
                    n = n.replace(',', '')
                    tmp.add_neighbour(n)
            valves[name] = tmp
    return valves

def value(valve, minutes):
    return valve.flow_rate * (minutes-valve.steps-1)

def steps(valves, start, goal):
    result = []
    visited = {}
    parent = { start : None }
    for key in valves.keys():
        visited[key] = False
    q = []
    q.append(start)
    visited[start] = True

    while len(q):
        cur = q.pop(0)
        
        if cur == goal:
            par = parent[cur]
            while par != None:
                result.insert(0, par)
                par = parent[par]
            return len(result)

        for neighbor in valves[cur].neighbors:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = cur

    return len(result)

def search(valves):
    cur = 'AA'
    q = []

    for key in valves.keys():
        valves[key].steps = steps(valves, cur, key)
        q.append([value(valves[key], 30), valves[key].name])
    
    q.sort(reverse=True)
    for v in q:
        #v[0] = steps(valves, cur, v)
        print(v.name, 'is', v.steps, 'away from AA.', v.flow_rate, '*', 30, '-1 =', v.value(30))
        print(v)

def part_1(valves):
    current_valve = valves['AA']
    search(valves)
    for minute in range(1, 31, 1):
        pass
        
        
        
        # # Print minute state
        # print('== Minute', minute, '==')
        # print('Valve', end=' ')
        # for key in valves.keys():
        #     if valves[key].open:
        #         print(valves[key].name, end=', ')
        # print("is open. Releasing", end=' ')
        # release = 0
        # for key in valves.keys():
        #     if valves[key].open:
        #         release += valves[key].flow_rate
        # print(release, 'pressure.')
        # print()
            


def part_2(valves):
    pass

print('Part 1:', part_1(read_input()))
print('Part 2:', part_2(read_input()))