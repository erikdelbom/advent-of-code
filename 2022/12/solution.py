from copy import deepcopy
def read_input():
    with open('data.in', 'r') as f:
        lines = list(map(str.rstrip, f.readlines()))
        result = []
        for l in lines:
            tmp = []
            for c in l:
                if c.islower():
                    val = ord(c)
                elif c == 'E':
                    val = 1000
                elif c == 'S':
                    val = ord('a')
                else:
                    val = c    
                tmp.append(val)
            result.append(tmp)
        return result

def search(data, width, height, start_x, start_y):
    visited = [[False for i in range(width)] for j in range(height)]
    frontier = []
    parent = [[None for i in range(width)] for j in range(height)]
    result = []

    # init
    frontier.append((start_x, start_y))
    visited[start_y][start_x] = True

    
    while len(frontier):
        x, y = frontier.pop(0)
        added = False

        if data[y][x] == 1000:
            result.append(deepcopy((x, y)))
            p_x, p_y = parent[y][x]
            while parent[p_y][p_x] != None:
                p_x, p_y = parent[p_y][p_x]
                result.append(deepcopy((p_x, p_y)))
            return len(result)
            
        if y > 0:
            if data[y][x] == 'S':
                frontier.append((x, y-1))
                visited[y-1][x] = True
                parent[y-1][x] = deepcopy((x, y))                
            elif not visited[y-1][x]:
                if data[y-1][x]-data[y][x] <= 1:
                    added = True
                    frontier.append((x, y-1))
                    visited[y-1][x] = True
                    parent[y-1][x] = deepcopy((x, y))
        if x < width-1:
            if data[y][x] == 'S':
                frontier.append((x+1, y))
                visited[y][x+1] = True
                parent[y][x+1] = deepcopy((x, y)) 
            elif not visited[y][x+1]:
                if data[y][x+1]-data[y][x] <= 1:
                    added = True
                    frontier.append((x+1, y))
                    visited[y][x+1] = True
                    parent[y][x+1] = (x, y)
        if y < height-1:
            if data[y][x] == 'S':
                frontier.append((x, y+1))
                visited[y+1][x] = True
                parent[y+1][x] = deepcopy((x, y))            
            elif not visited[y+1][x]:
                if data[y+1][x]-data[y][x] <= 1:
                    added = True
                    frontier.append((x, y+1))
                    visited[y+1][x] = True
                    parent[y+1][x] = deepcopy((x, y))
        if x > 0:
            if data[y][x] == 'S':
                frontier.append((x-1, y))
                visited[y][x-1] = True
                parent[y][x-1] = deepcopy((x, y)) 
            elif not visited[y][x-1]:
                if data[y][x-1]-data[y][x] <= 1:
                    added = True
                    frontier.append((x-1, y))
                    visited[y][x-1] = True
                    parent[y][x-1] = deepcopy((x, y))
        

        if not added:
            if y > 0:
                if data[y-1][x] == 1000:
                    frontier.append((x, y-1))
                    visited[y-1][x] = True
                    parent[y-1][x] = deepcopy((x, y))
            if x > 0:
                if data[y][x-1] == 1000:
                    frontier.append((x-1, y))
                    visited[y][x-1] = True
                    parent[y][x-1] = deepcopy((x, y))
            if y < height-1:
                if data[y+1][x] == 1000:
                        frontier.append((x, y+1))
                        visited[y+1][x] = True
                        parent[y+1][x] = deepcopy((x, y))
            
            if x < width-1:
                if data[y][x+1] == 1000:
                    frontier.append((x+1, y))
                    visited[y][x+1] = True
                    parent[y][x+1] = deepcopy((x, y))
    
    return len(result)

def part_1(data):
    for l in data:
        print(l)
    width = len(data[0])
    height = len(data)
    s_x = 0
    s_y = 0

    # Find start pos
    for i in range(height):
        for j in range(width):
            if data[i][j] == 'S': #or data[i][j] == 97:
                s_x = j
                s_y = i
                break
    
    visited = [[False for i in range(width)] for j in range(height)]
    frontier = []
    parent = [[None for i in range(width)] for j in range(height)]
    result = []

    # init
    frontier.append((s_x, s_y))
    visited[s_y][s_x] = True

    
    while len(frontier):
        x, y = frontier.pop(0)
        added = False

        if data[y][x] == 1000:
            result.append(deepcopy((x, y)))
            p_x, p_y = parent[y][x]
            while parent[p_y][p_x] != None:
                p_x, p_y = parent[p_y][p_x]
                result.append(deepcopy((p_x, p_y)))
            print(result)
            return len(result)
            
        print(x, y)
        if y > 0:
            if data[y][x] == 'S':
                frontier.append((x, y-1))
                visited[y-1][x] = True
                parent[y-1][x] = deepcopy((x, y))                
                print("Adding", x, y-1)
            elif not visited[y-1][x]:
                if data[y-1][x]-data[y][x] <= 1:
                    added = True
                    print("Adding", x, y-1)
                    frontier.append((x, y-1))
                    visited[y-1][x] = True
                    parent[y-1][x] = deepcopy((x, y))
        if x < width-1:
            if data[y][x] == 'S':
                frontier.append((x+1, y))
                visited[y][x+1] = True
                parent[y][x+1] = deepcopy((x, y)) 
                print("Adding", x+1, y)
            elif not visited[y][x+1]:
                if data[y][x+1]-data[y][x] <= 1:
                    added = True
                    print("Adding", x+1, y)
                    frontier.append((x+1, y))
                    visited[y][x+1] = True
                    parent[y][x+1] = (x, y)
        if y < height-1:
            if data[y][x] == 'S':
                frontier.append((x, y+1))
                visited[y+1][x] = True
                parent[y+1][x] = deepcopy((x, y))            
                print("Adding", x, y+1)
            elif not visited[y+1][x]:
                if data[y+1][x]-data[y][x] <= 1:
                    added = True
                    print("Adding", x, y+1)
                    frontier.append((x, y+1))
                    visited[y+1][x] = True
                    parent[y+1][x] = deepcopy((x, y))
        if x > 0:
            if data[y][x] == 'S':
                frontier.append((x-1, y))
                visited[y][x-1] = True
                parent[y][x-1] = deepcopy((x, y)) 
                print("Adding", x-1, y)
            elif not visited[y][x-1]:
                if data[y][x-1]-data[y][x] <= 1:
                    added = True
                    print("Adding", x-1, y)
                    frontier.append((x-1, y))
                    visited[y][x-1] = True
                    parent[y][x-1] = deepcopy((x, y))
        

        if not added:
            if y > 0:
                if data[y-1][x] == 1000:
                    frontier.append((x, y-1))
                    visited[y-1][x] = True
                    parent[y-1][x] = deepcopy((x, y))
            if x > 0:
                if data[y][x-1] == 1000:
                    frontier.append((x-1, y))
                    visited[y][x-1] = True
                    parent[y][x-1] = deepcopy((x, y))
            if y < height-1:
                if data[y+1][x] == 1000:
                        frontier.append((x, y+1))
                        visited[y+1][x] = True
                        parent[y+1][x] = deepcopy((x, y))
            
            if x < width-1:
                if data[y][x+1] == 1000:
                    frontier.append((x+1, y))
                    visited[y][x+1] = True
                    parent[y][x+1] = deepcopy((x, y))
    
        print()
    return len(result)


def part_2(data):
    for l in data:
        print(l)
    width = len(data[0])
    height = len(data)
    s_x = 0
    s_y = 0

    results = []

    # Find start pos
    for i in range(height):
        for j in range(width):
            if data[i][j] == 97:
                s_x = j
                s_y = i
                results.append(search(data, width, height, s_x, s_y))

    return results

print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))
