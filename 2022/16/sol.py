from copy import copy

class Valve: 
    def __init__(self, name, flow_rate):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = []
        self.distances = {}

    def add_neighbor(self, name):
        self.neighbors.append(name)

    def print(self):
        print('Name:', self.name)
        print('Flow rate: ', self.flow_rate)
        print('Distances:', self.distances)

def read_input():
    valves = {}
    with open('test.in') as f:
        for line in f:
            valve_info, neighbor_info = line.split(';')
            name = valve_info.split()[1]
            fr = int(valve_info.split('=')[1])
            tmp = Valve(name, fr)
            neighbors = neighbor_info.split('valve')[1].split()
            for n in neighbors:
                if n != 's':
                    n = n.replace(',', '')
                    tmp.add_neighbor(n)
                valves[name] = tmp
    return valves

def bfs(valves, start, goal):
    if start == goal:
        return []

    result = []
    visited = {}
    parent = { start : start }
    for key in valves.keys():
        visited[key] = False
    q = []
    q.append(start)
    visited[start] = True

    while len(q):
        cur = q.pop(0)
        
        if cur == goal:
            par = parent[cur]
            result.append(cur)
            while par != start:
                result.insert(0, par)
                par = parent[par]
            return result
        
        for neighbor in valves[cur].neighbors:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = cur
    
    return result

def all_open(opened):
    for key in opened.keys():
        if not opened[key]:
            return False
    return True

def get_minute_score(valves, opened):
    sum = 0
    for key in valves.keys():
        if opened[key]:
            sum += valves[key].flow_rate 
    return sum

def predicted_value():
    pass

def search(valves, start, minute, opened, path_key, paths, score):
    score += get_minute_score(valves, opened)
    path_key += start
    previous = path_key[-4:-2]

    if all_open(opened):
        paths[path_key] = score + (30-minute+1) * get_minute_score(valves, opened)    
    elif minute >= 29:
        paths[path_key] = score 
        return 
    
    other_found = False
    for n in valves[start].neighbors:
        if n == previous:
            continue
        other_found = True
        search(valves, n, minute+1, copy(opened), path_key, paths, score)
        if valves[n].flow_rate > 0 and not opened[n]:
            score += get_minute_score(valves, opened)
            opened_copy = copy(opened)
            opened_copy[n] = True
            if minute < 28:
                search(valves, n, minute+2, opened_copy, path_key+'!', paths, score)
    
    if not other_found:
        search(valves, previous, minute+1, copy(opened), path_key, paths, score)
        if valves[previous].flow_rate > 0 and not opened[previous]:
            score += get_minute_score(valves, opened)
            opened_copy = copy(opened)
            opened_copy[previous] = True
            #score -= valves[previous].flow_rate
            if minute < 28:
                search(valves, previous, minute+2, opened_copy, path_key+'!', paths, score)
        

def part_1(valves):
    # Calculate distance between all valves
    # for key in valves.keys():
    #    for goal in valves.keys():
    #        valves[key].distances[goal] = len(bfs(valves, key, goal))
    #    valves[key].print()    
        
    paths = {}
    opened = {}
    for key in valves.keys():
        opened[key] = False

    search(valves, 'AA', 0, opened, '', paths, 0)
    
    max_score = 0
    max_key = ''
    for key in paths.keys():
        if paths[key] > max_score:
            max_score = paths[key]
            max_key = key
    print(max_key)
    return max_score

print('Part 1:', part_1(read_input()))
