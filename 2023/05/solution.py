import sys

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


def lookup(conns, source):
    result = source
    for conn in conns:
        s_start, s_end = conn["source_start"], conn["source_end"]
        d_start = conn["dest_start"]
        if source >= s_start and source <= s_end:
            diff = source - s_start
            result = d_start + diff
    return result


def part_1(data):
    minimum = 10000000000000000000
    parts = []
    part = []
    for line in data:
        if line == '':
            parts.append(part)
            part = []
        else:
            part.append(line)
    parts.append(part)
    seeds = list(map(int, parts[0][0].split(': ')[1].split()))

    map_dict = {}    

    for part in parts:
        key = part[0].split(' map:')[0]
        part.pop(0)
        connections = []
        for subpart in part:
            subpart = list(map(int, subpart.split()))
            source_start, source_end = subpart[1], subpart[1]+(subpart[2]-1)
            dest_start, dest_end = subpart[0], subpart[0]+(subpart[2]-1)
            tmp = {"source_start": source_start, "source_end": source_end, "dest_start": dest_start, "dest_end": dest_end}            
            connections.append(tmp) 
        map_dict[key] = connections
    for seed in seeds:
        soil = lookup(map_dict["seed-to-soil"], seed)
        fert = lookup(map_dict["soil-to-fertilizer"], soil)
        water = lookup(map_dict["fertilizer-to-water"], fert)
        light = lookup(map_dict["water-to-light"], water)
        temp = lookup(map_dict["light-to-temperature"], light)
        humi = lookup(map_dict["temperature-to-humidity"], temp)
        loc = lookup(map_dict["humidity-to-location"], humi)

        minimum = min([loc, minimum])
         
    return minimum    

    
    

def part_2(data):
    minimum = 10000000000000000000
    parts = []
    part = []
    for line in data:
        if line == '':
            parts.append(part)
            part = []
        else:
            part.append(line)
    parts.append(part)
    seeds = list(map(int, parts[0][0].split(': ')[1].split()))

    map_dict = {}    

    for part in parts:
        key = part[0].split(' map:')[0]
        part.pop(0)
        connections = []
        for subpart in part:
            subpart = list(map(int, subpart.split()))
            source_start, source_end = subpart[1], subpart[1]+(subpart[2]-1)
            dest_start, dest_end = subpart[0], subpart[0]+(subpart[2]-1)
            tmp = {"source_start": source_start, "source_end": source_end, "dest_start": dest_start, "dest_end": dest_end}            
            connections.append(tmp) 
        map_dict[key] = connections

    lowest = 1000000000000000000
    for item in map_dict["humidity-to-location"]:
        if item["dest_start"] < lowest:
            lowest

    for i in range(0, len(seeds), 2):
        for j in range(seeds[i+1]):
            
         
    return minimum    


input_file = sys.argv[1]

print("Part 1:", part_1(read_input(input_file)))
print("Part 2:", part_2(read_input(input_file)))
