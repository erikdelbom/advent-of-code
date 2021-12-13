def search(graph, start, end):
    found_way = []
    
    graph[start].visited = True
    graph[start].parent = 'start'
    queue = []
    queue.append(start)

    while len(queue) != 0:
        current_node = queue[0]
        queue.pop(0)

        for n in graph[current_node].neighbours:
            if n == end:
                found_way.append(n)
                found_way.append(current_node)
                while current_node != 'start':
                    current_node = graph[current_node].parent
                    found_way.append(current_node)
                found_way.reverse()
                return found_way
            
            if not graph[n].visited:
                queue.append(n)
                graph[n].parent = current_node
                graph[n].visited == True

    return found_way