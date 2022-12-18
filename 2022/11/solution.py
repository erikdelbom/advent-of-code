class Monkey:
    def __init__(self):
        self.items = []
        self.op = None
        self.test = None
        self.target = [None, None]
        self.op_val = None
        self.test_val = None
        self.count = 0

def read_input():
    with open('data.in', 'r') as f:
        monkeys = []
        m = Monkey()
        for line in list(map(str.strip, f.readlines())):
            if line == '':
                monkeys.append(m)
                m = Monkey()
                continue
            try:
                var, arg = line.split(': ')
                if var == 'Starting items':
                    for a in arg.split(', '):
                        m.items.append(int(a))

                elif var == 'Operation':
                    op_t = arg[10]
                    val = arg.split()[-1]
                    
                    if op_t == '+':
                        if val == 'old':
                            m.op = lambda a, b=a : a + a
                        else:
                            m.op_val = int(val)
                            m.op = lambda a, b : a + b

                    elif op_t == '*':
                        if val == 'old':
                            m.op = lambda a, b=a : a * a
                        else:
                            m.op_val = int(val)
                            m.op = lambda a, b : a * b
                    
                elif var == 'Test':
                    m.test_val = int(arg.split()[-1])
                    m.test = lambda a, b : a % b

                elif var == 'If true':
                    m.target[1] = int(arg.split()[-1])

                elif var == 'If false':
                    m.target[0] = int(arg.split()[-1])
                
            except:
                continue

    monkeys.append(m)
    return monkeys

def part_1(data):
    for round in range(20):
        for monkey in data:
            monkey.count += len(monkey.items)
            for i in range(len(monkey.items)):
                item_value = monkey.items[i] 
                item_value = int(monkey.op(item_value, monkey.op_val) / 3)
                monkey.items[i] = item_value
                next = monkey.target[1] if monkey.test(item_value, monkey.test_val) == 0 else monkey.target[0]
                data[next].items.append(item_value)
            monkey.items = []
    def func(d):
        return d.count
    data.sort(reverse=True, key=func)

    return data[0].count * data[1].count


def part_2(data):
    mod = 1
    for m in data:
        mod *= m.test_val

    for round in range(10000):
        for monkey in data:
            monkey.count += len(monkey.items)
            for i in range(len(monkey.items)):
                item_value = monkey.items[i]
                item_value = monkey.op(item_value, monkey.op_val) % mod
                next = monkey.target[1] if monkey.test(item_value, monkey.test_val) == 0 else monkey.target[0]
                data[next].items.append(item_value)
            monkey.items = []
    
    #     for idx, m in enumerate(data):
    #         print(str(i) + ':', end=' ')
    #         for it in m.items:
    #             print(it, end=' ')
    #         print()
    #     print()
    # for m in data:
    #     print(m.count)

    def func(d):
        return d.count
    data.sort(reverse=True, key=func)

    return data[0].count * data[1].count

print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))
            
# for idx, m in enumerate(read_input()):
#     print("Monkey:", idx)
#     print("Items:", m.items)
#     print("Op:", m.op(3, m.op_val))
#     print("Test:", m.test(3, m.test_val))
