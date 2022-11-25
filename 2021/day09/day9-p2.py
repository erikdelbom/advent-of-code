import sys

height_map = []
visited = []
visited_count = 0
row_length = 0

for line in sys.stdin:
    row_length = len(line)-1
    for c in line:
        if c != '\n':
            height_map.append(int(c))
            visited.append(False)

all_basins = []

for i in range(len(height_map)):
    basin_sum = 0
    queue = []

    if height_map[i] != 9 and not visited[i]:
        queue.append(i)
        visited[i] = True
        basin_sum += 1
    
    while len(queue) != 0:
        current = queue[0]
        queue.pop(0)
        
        # Look for north neighbour
        if current >= row_length:
            if height_map[current-row_length] != 9 and not visited[current-row_length]:
                queue.append(current-row_length)
                visited[current-row_length] = True
                basin_sum += 1

        # Look for east neighbour
        if (current % (row_length) != (row_length-1) or current == 0) and current != (len(height_map)-1):
            if height_map[current+1] != 9 and not visited[current+1]:
                queue.append(current+1)
                visited[current+1] = True
                basin_sum += 1

        # Look for south neighbour
        if current < (len(height_map)-row_length):
            if height_map[current+row_length] != 9 and not visited[current+row_length]:
                queue.append(current+row_length)
                visited[current+row_length] = True
                basin_sum += 1

        # Look for west neighbour
        if current % row_length != 0 and current != 0:
            if height_map[current-1] != 9 and not visited[current-1]:
                queue.append(current-1)
                visited[current-1] = True
                basin_sum += 1

    if basin_sum != 0:
        all_basins.append(basin_sum)
        
total = 1

for i in range(3):
    max_basin = max(all_basins)
    total *= max_basin
    all_basins.remove(max_basin)

print(total)