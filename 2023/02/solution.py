
def read_input():
    with open('data.in', 'r') as f:
        return list(map(str.rstrip, f.readlines()))

max_table = { "red" : 12, "green" : 13, "blue" : 14 }


def part_1(data_list):
    sum = 0
    for idx, data in enumerate(data_list):
        valid = True
        count_table = { "red" : 0, "green" : 0, "blue" : 0 }
        sets = data.split(": ")[1].split('; ')

        for se in sets:
            colors = se.split(', ')
            for color in colors:
                for key in max_table.keys():
                    key_idx = color.find(key)
                    if key_idx > 0:
                        amount = int(color[0:key_idx-1])
                        

                        if amount > max_table[key]:
                            valid = False

        if valid:
            sum += idx+1

    return sum

def part_2(data_list):
    sum = 0
    for idx, data in enumerate(data_list):
        count_table = { "red" : 0, "green" : 0, "blue" : 0 }
        sets = data.split(": ")[1].split('; ')

        for se in sets:
            colors = se.split(', ')
            for color in colors:
                for key in max_table.keys():
                    key_idx = color.find(key)
                    if key_idx > 0:
                        amount = int(color[0:key_idx-1])
                        count_table[key] = max([amount, count_table[key]])
        
        power = 1
        for item in count_table.values():
            power *= item
        sum += power
    return sum

print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))
