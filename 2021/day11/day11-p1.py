import sys

width = 0
height = 0
octos = []

for line in sys.stdin:
    height += 1
    line = line.strip()
    width = len(line)
    for c in line:
        octos.append(int(c))

def find_neighbours(list, current):
    neighbours = []

    # North neigbour
    if current >= width:
        neighbours.append(current-width)

    # North east neighbour
    if current % width != (width-1) and current >= width:
        neighbours.append(current-width+1)

    # North west neighbour
    if current % width != 0 and current >= width:
        neighbours.append(current-width-1)

    # East neighbour
    if current % width != (width-1):
        neighbours.append(current+1)

    # West neighbour
    if current % width != 0:
        neighbours.append(current-1)

    # South neighbour
    if current < (len(list)-width):
        neighbours.append(current+width)

    # South west neighbour
    if current < (len(list)-width) and current % width != 0:
        neighbours.append(current+width-1)
    
    # South east neighbour
    if current < (len(list)-width) and current % width != (width-1):
        neighbours.append(current+width+1)

    return neighbours

def update_neigbours(octos, neighbours):
    for n in neighbours:
        if octos[n] != 0 and octos[n] != -1:
            octos[n] += 1
        if octos[n] > 9:
            octos[n] = -1
            update_neigbours(octos, find_neighbours(octos, n))

total = 0

for day in range(100):
    flashes = 0

    for i in range(len(octos)):
        octos[i] += 1
        if octos[i] > 9:
            octos[i] = 0
    
    for i in range(len(octos)):
        if octos[i] == 0:
            update_neigbours(octos, find_neighbours(octos, i))
            
    for i in range(len(octos)):
        if octos[i] == 0 or octos[i] == -1:
            flashes += 1
            octos[i] = 0

    total += flashes

print(total)