def read_input():
    with open('data.in', 'r') as f:
        result = []
        for line in f.readlines():
            coords = tuple(map(int, line.strip().split(',')))
            result.append(coords)
    return result

def adjacent(cube_1, cube_2):
    one_off = 0
    two_common = 0
    for i in range(3):
        if cube_1[i] == cube_2[i]:
            two_common += 1
        elif abs(cube_1[i] - cube_2[i]) == 1:
            one_off += 1
    return one_off == 1 and two_common == 2

def part_1(cubes):
    surfaces = 0
    for cube in cubes:
        adj = 0
        for other_cube in cubes:
            if cube != other_cube:
                if adjacent(cube, other_cube):
                   adj += 1
        surfaces += 6 - adj
    return surfaces

def bfs(cubes):
    min_x = min(cube[0] for cube in cubes) - 1
    max_x = max(cube[0] for cube in cubes) + 1
    min_y = min(cube[1] for cube in cubes) - 1
    max_y = max(cube[1] for cube in cubes) + 1
    min_z = min(cube[2] for cube in cubes) - 1
    max_z = max(cube[2] for cube in cubes) + 1
    start = (min_x, min_y, min_z)

    surface_count = 0
    visited = {}
    for z in range(min_z, max_z+1, 1):
        for y in range(min_y, max_y+1, 1):
            for x in range(min_x, max_x+1, 1):
                visited[(x, y, z)] = False
    frontier = []

    frontier.append(start)
    visited[start] = True

    while len(frontier):
        cur = frontier.pop(0)

        if cur[0] > min_x:
            next = (cur[0]-1, cur[1], cur[2])
            if not visited[next]:
                if next in cubes:
                    surface_count += 1
                else:
                    visited[next] = True
                    frontier.append(next)

        if cur[0] < max_x:
            next = (cur[0]+1, cur[1], cur[2])
            if not visited[next]:
                if next in cubes:
                    surface_count += 1
                else:
                    visited[next] = True
                    frontier.append(next)

        if cur[1] > min_y:
            next = (cur[0], cur[1]-1, cur[2])
            if not visited[next]:
                if next in cubes:
                    surface_count += 1
                else:
                    visited[next] = True
                    frontier.append(next)
        
        if cur[1] < max_y:
            next = (cur[0], cur[1]+1, cur[2])
            if not visited[next]:
                if next in cubes:
                    surface_count += 1
                else:
                    visited[next] = True
                    frontier.append(next)

        if cur[2] > min_z:
            next = (cur[0], cur[1], cur[2]-1)
            if not visited[next]:
                if next in cubes:
                    surface_count += 1
                else:
                    visited[next] = True
                    frontier.append(next)

        if cur[2] < max_z:
            next = (cur[0], cur[1], cur[2]+1)
            if not visited[next]:
                if next in cubes:
                    surface_count += 1
                else:
                    visited[next] = True
                    frontier.append(next)

    return surface_count

def part_2(cubes):
    return bfs(cubes)
  
print('Part 1:', part_1(read_input()))
print('part 2:', part_2(read_input()))
