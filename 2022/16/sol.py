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
    for key in opened.keys():
        if valves[key].flow_rate >= 1 and opened[key]:
            sum += valves[key].flow_rate 
    return sum

def predicted_value():
    pass

def calc_score_lims():
    pass

def search(valves, start, minute, opened, path_key, paths, score):
    score[minute] = get_minute_score(valves, opened)

    if sum(score) < 20 and minute > 4:
        return
    if sum(score) < 300 and minute > 15:
        return

    if all_open(opened):
        for i in range(30-minute):
            score[minute+i] = get_minute_score(valves, opened)
        paths[path_key] = score
        return
    elif minute >= 29:
        #score[minute] = get_minute_score(valves, opened)
        paths[path_key] = score 
        return 

    #print(path_key)

    for node in opened.keys():
        if node != start:
            if len(path_key) >= 3*2:
                path_key_copy = path_key.replace('!', '')
                p1 = path_key_copy[-6:-4]
                p2 = path_key_copy[-4:-2]
                p3 = path_key_copy[-2:]
                if p1 == p3 and node == p2:
                    continue
            distance = valves[start].distances[node]
            if valves[node].flow_rate >= 15:
                if not opened[node] and 29-minute > distance+1:
                    for i in range(distance+1):
                        score[minute+i] = get_minute_score(valves, opened)
                    opened_copy = copy(opened)
                    opened_copy[node] = True
                    search(valves, node, minute+distance+1, opened_copy, path_key+'!'+node, paths, copy(score))
            else:
                if 29 - minute > distance:
                    for i in range(distance+1):
                        score[minute+i] = get_minute_score(valves, opened)
                    search(valves, node, minute+distance, copy(opened), path_key+node, paths, copy(score))
                if not opened[node] and 29-minute > distance+1:
                    opened_copy = copy(opened)
                    opened_copy[node] = True
                    search(valves, node, minute+distance+1, opened_copy, path_key+'!'+node, paths, copy(score))

def part_1(valves):
    # Calculate distance between all valves
    for key in valves.keys():
        for goal in valves.keys():
            valves[key].distances[goal] = len(bfs(valves, key, goal))
        
    paths = {}
    opened = {}
    for key in valves.keys():
        for n in valves[key].neighbors:
            if valves[n].flow_rate < 1:
                #print('remove', n)
                valves[key].neighbors.remove(n)
        if valves[key].flow_rate > 0:
            opened[key] = False

    #print(opened)

    search(valves, 'AA', 0, opened, '', paths, [0 for i in range(30)])
    print('search done')
    max_score = 0
    max_key = ''
    for key in paths.keys():
        if sum(paths[key]) > max_score:
            max_score = sum(paths[key])
            max_key = key
    return max_score

print('Part 1:', part_1(read_input()))
