import sys
import math
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


def lookup(connections, source):
    result = source
    for conn in connections:
        s_start, s_end = conn["source_start"], conn["source_end"]
        d_start = conn["dest_start"]
        if source >= s_start and source <= s_end:
            diff = source - s_start
            result = d_start + diff
    return result


def reverse_lookup(connections, dest):
    for conn in connections:
        d_start, d_end = conn["dest_start"], conn["dest_end"]
        s_start = conn["source_start"]
        if dest >= d_start and dest <= d_end:
            diff = dest - d_start



def get_conversion_maps(data):
    conversion_maps = []
    conversion_map = []
    for line in data:
        if line == '':
            conversion_maps.append(conversion_map)
            conversion_map = []
        else:
            conversion_map.append(line)
    conversion_maps.append(conversion_map)
    return conversion_maps

def convert_to_dict(conversion_maps_list):
    conversion_maps = {}
    for conversion_map in conversion_maps_list:
        key = conversion_map[0].split(' map:')[0]
        conversion_map.pop(0)
        connections = []
        for connection in conversion_map:
            connection = list(map(int, connection.split()))
            source_start, source_end = connection[1], connection[1]+(connection[2]-1)
            dest_start, dest_end = connection[0], connection[0]+(connection[2]-1)
            tmp = {"source_start": source_start, "source_end": source_end, "dest_start": dest_start, "dest_end": dest_end}            
            connections.append(tmp) 
        #conversion_maps.append(connections)
        conversion_maps[key] = connections

    return conversion_maps


def trace_to_end(conversion_maps, start_idx, value):
    if start_idx == 7:
        return value
    next_value = lookup(conversion_maps[start_idx+1], value)
    trace_to_end(conversion_maps, start_idx+1, next_value)


def create_lowest_table(conversion_maps):
    result = []
    for key, value in conversion_maps.items():
        for item in value:
            "dest_start"


def find_lowest(lowest_maps, prev_lowest):
    pass
    
    
    
    # for idx, conversion_map in enumerate(conversion_maps):
    #     candidate = value["dest_start"]
    #     if candidate <= prev_lowest:
    #         prev_lowest = candidate
    #         # check if value holds until location
    #         if candidate == trace_to_end(conversion_maps, )

    #         # check if can be traced back to seed




def part_1(data):
    minimum = math.inf
    conversion_maps_list = get_conversion_maps(data)
    seeds = list(map(int, conversion_maps_list[0][0].split(': ')[1].split()))
    conversion_maps_list.pop(0)   
    conversion_maps = convert_to_dict(conversion_maps_list)

    done = True
    lowest_table = create_lowest_table(conversion_maps)
    lowest = find_lowest(lowest_table)
    while not done:
        lowest = find_lowest(conversion_maps, lowest)

    # for seed in seeds:
    #     soil = lookup(conversion_maps["seed-to-soil"], seed)
    #     fert = lookup(conversion_maps["soil-to-fertilizer"], soil)
    #     water = lookup(conversion_maps["fertilizer-to-water"], fert)
    #     light = lookup(conversion_maps["water-to-light"], water)
    #     temp = lookup(conversion_maps["light-to-temperature"], light)
    #     humi = lookup(conversion_maps["temperature-to-humidity"], temp)
    #     loc = lookup(conversion_maps["humidity-to-location"], humi)

    #     minimum = min([loc, minimum])
         
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
    lowest_item = {}
    for item in map_dict["humidity-to-location"]:
        if item["dest_start"] < lowest:
            lowest = item["dest_start"]
            lowest_item = item
    
    print(lowest)

    for item in map_dict["temperature-to humidity"]:
        if lowest_item <= item["dest_start"]:
            pass
    #for i in range(0, len(seeds), 2):
    #    for j in range(seeds[i+1]):
            
         
    return minimum    


input_file = sys.argv[1]


start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")

#82 -> 84 -> 84 -> 84 -> 77 -> 45 -> 46 -> 46