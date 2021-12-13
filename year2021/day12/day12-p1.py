import sys

class Node:
    def __init__(self, namep):
        self.name = namep
        self.visited = False
        self.neighbours = []
        self.parent = ''
       
def search(graph, start, end, path):
    count = 0
    path.append(start)
    
    if start.islower():
        graph[start].visited = True

    for n in graph[start].neighbours:
        if n == end:
            count += 1
        
        elif not graph[n].visited:
            count += search(graph, n, end, path)
    
    latest = path.pop()
    graph[latest].visited = False

    return count

graph = {}

for line in sys.stdin:
    line = line.strip()
    first_node, second_node = line.split('-')
    
    if first_node not in graph:
        graph[first_node] = Node(first_node)
    if second_node not in graph:
        graph[second_node] = Node(second_node)

    graph[first_node].neighbours.append(second_node)
    graph[second_node].neighbours.append(first_node)

path = []
count = search(graph, 'start', 'end', path)

print('Part 1:', count)