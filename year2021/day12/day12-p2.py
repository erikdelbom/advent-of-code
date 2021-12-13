import sys

class Node:
    def __init__(self, namep):
        self.name = namep
        self.visited = False
        self.neighbours = []
        self.parent = ''
        self.visited_count = 0

def print_path(path):
    for i in range(len(path)):
        if i == len(path)-1:
            print(path[i])
        else:
            print(path[i], end=' - ')
    
def search(graph, node, counter):
    if node == 'end':
        return 1
    for n in graph[node].neighbours:
        if n.isupper():
            counter += search(graph, n, 0)
        elif not graph[n].visited:
            graph[n].visited = True
            counter += search(graph, n, 0)
            graph[n].visited = False
    return counter
    
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

graph['start'].visited = 1

sum = 0
sum += search(graph, 'start', 0)
    
print(sum)