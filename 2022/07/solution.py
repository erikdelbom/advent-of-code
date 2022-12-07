def read_input():
    with open('data.in', 'r') as f:
        return list(map(str.rstrip, f.readlines()))

class Node:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def add_child(self, obj):
        for child in self.children:
            if obj.name == child.name:
                return child
        self.children.append(obj)
        return obj

    def get_size(self):
        total = 0
        for child in self.children:
            if child.size > 0:
                total += child.size
            else:
                total += child.get_size()
        return total

    def sum_directories(self, n):
        result = 0
        for child in self.children:
            result += child.sum_directories(n)
            if child.get_size() <= n:
                result += child.get_size()
        return result

    def find_directory(self, n, smallest):
        for child in self.children:
            if child.get_size() >= n and child.get_size() < smallest:
                smallest = child.find_directory(n, child.get_size())
        return smallest
        

def build_system(data):
    root = Node('/', 0, None)
    cur = root
    
    for i in range(1, len(data)):
        line = data[i].split()
        cmd = line[1]
        if cmd == 'cd':
            arg = line[2]
            if arg != '..':
                cur = cur.add_child(Node(arg, -1, cur))
            elif arg == '..':
                cur = cur.parent
        elif cmd == 'ls':
            i += 1
            for j in range(i, len(data)):
                if data[i].split()[0] == '$':
                    break
                f_info, f_name = data[i].split()
                if f_info == 'dir':
                    cur.add_child(Node(f_name, -1, cur))
                else:
                    cur.add_child(Node(f_name, int(f_info), cur))
                i += 1
            i -= 1

    return root

def part_1(data):
    system = build_system(data)
    return system.sum_directories(100000)

def part_2(data):
    system = build_system(data)
    req_space = 30000000 - (70000000 - system.get_size())
    return system.find_directory(req_space, system.get_size())

print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))
