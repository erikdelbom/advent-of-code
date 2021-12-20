from sys import stdin

width = 0
map = []
visited = []
parent = []

for line in stdin:
    line = line.strip()
    width = len(line)
    for c in line:
        if c != '\n':
            map.append(int(c))
            visited.append(False)
            parent.append(0)



def find_neighbours(list, current):
    neighbours = []

    # North neigbour
    if current >= width:
        neighbours.append(current-width)

    # East neighbour
    if current % width != (width-1):
        neighbours.append(current+1)

    # West neighbour
    if current % width != 0:
        neighbours.append(current-1)

    # South neighbour
    if current < (len(list)-width):
        neighbours.append(current+width)

    return neighbours

def by_value(elem):
    return elem[1]

def search(map):
    queue = []
    queue.append([0, 0])
    visited[0] = True
    path =  []

    while len(queue) != 0:
        current = int(queue[0][0])
        current_cost = queue[0][1]
        queue.pop(0)
        for n in find_neighbours(map, current):
            if n == (len(map) - 1):
                path = [n, current]
                p = parent[current]
                while p != 0:
                    path.append(p)
                    p = parent[p]
                return path  
            if not visited[n]:
                queue.append([n, map[n]+current_cost])
                visited[n] = True
                parent[n] = current
        queue.sort(key=by_value)
    return path

cost = 0
for i in search(map):
    cost += map[i]
print(cost)