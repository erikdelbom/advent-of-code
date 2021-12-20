from sys import stdin

def update_row(row):
    for i in range(len(row)):
        if row[i] == 9:
            row[i] = 1
        else:
            row[i] += 1

def complete_map(map, width):
    complete = []
    height = int(len(map) / width)
    for row in range(height):
        cur_row = []
        for col in range(width):
            current = row * width + col
            cur_row.append(map[current])
            complete.append(map[current])
        for i in range(4):
            update_row(cur_row)
            for c in cur_row:
                complete.append(c)
    
    for row in range(height*4):
        cur_row = []
        for col in range(width*5):
            current = row * width*5 + col
            cur_row.append(complete[current])
        update_row(cur_row)
        for c in cur_row:
            complete.append(c)

    return complete

def find_neighbours(list, current, width):
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

def search(map, width):
    height = int(len(map) / width)
    visited = [False] * width * height
    parent = [0] * width * height

    path = []
    queue = []
    
    queue.append([0, 0])
    visited[0] = True

    while len(queue) != 0:
        current = int(queue[0][0])
        current_cost = queue[0][1]
        queue.pop(0)
        for n in find_neighbours(map, current, width):
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

width = 0
map = []

for line in stdin:
    line = line.strip()
    width = len(line)
    for c in line:
        if c != '\n':
            map.append(int(c))

big_map = complete_map(map, width)
width *= 5
cost = 0

path = search(big_map, width)
for i in path:
    cost += big_map[i]
print(cost)