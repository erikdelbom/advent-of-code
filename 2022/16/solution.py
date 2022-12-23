from copy import copy

def read_input():
    valves = []
    neighbors = {}
    flow_rate = {}

    with open('data.in', 'r') as f:
        for line in f.readlines():
            valve_info, neighbor_info = line.split(';')
            name = valve_info.split()[1]
            valves.append(name)
            neighbors[name] = []
            fr = int(valve_info.split('=')[1])
            flow_rate[name] = fr
            ns = neighbor_info.split('valve')[1].split()
            for n in ns:
                if n != 's':
                    n = n.replace(',', '')
                    neighbors[name].append(n)
        
        return (valves, neighbors, flow_rate)

def bfs(neighbors, start, goal):
    if start == goal: 
        return 0

    visited = {}
    
    for key in neighbors.keys():
        visited[key] = False
    
    q = []
    q.append((start, 0))
    visited[start] = True

    while len(q):
        cur, steps = q.pop(0)

        for neighbor in neighbors[cur]:
            if neighbor == goal:
                return steps+1
            if not visited[neighbor]:
                q.append((neighbor, steps+1))
                visited[neighbor] = True

    return -1

def part_1(data):
    valves, neighbors, flow_rate = data
    distance = {}

    for start in valves:
        distance[start] = {}
        for goal in valves:
            distance[start][goal] = bfs(neighbors, start, goal)
    
    valves_to_open = [valve for valve in valves if flow_rate[valve] > 0]

    max_score = 0
    time_limit = 30
    path_stack = []
    path_stack.append([['AA'], 0, {}])

    while len(path_stack):
        path, elapsed, opened = path_stack.pop()
        current_valve = path[-1]

        if elapsed >= time_limit or len(path) == len(valves_to_open)+1:
            result = 0
            for valve, time_opened in opened.items():
                minutes = max(time_limit - time_opened, 0)
                result += minutes * flow_rate[valve] 
            
            max_score = max(result, max_score)
        
        else:
            for next_valve in valves_to_open:
                if next_valve not in opened.keys():
                    
                    time_opened = elapsed + distance[current_valve][next_valve] + 1
                    
                    opened_copy = copy(opened)
                    opened_copy[next_valve] = time_opened
                    
                    path_copy = copy(path)
                    path_copy.append(next_valve)

                    path_stack.append([path_copy, time_opened, opened_copy])
    
    return max_score

            


    

print('Part 1:', part_1(read_input()))