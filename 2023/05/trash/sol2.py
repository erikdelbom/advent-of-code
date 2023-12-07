import sys
import math
import time
import copy

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


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
    conversion_maps = []
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
        conversion_maps.append(connections)
        #conversion_maps[key] = connections

    return conversion_maps


def create_lowest_table(seeds, conversion_maps):
    result = []

    for value in conversion_maps:
        res = []
        for item in value:
            res.append([item["dest_start"], item["dest_end"]])
        result.append(res)
    return result


def find_lowest(lowest_maps):
    lowest = math.inf
    top_idx = None
    nested_idx = None
    for t_idx, value in enumerate(lowest_maps):
        for n_idx, candidate in enumerate(value):
            if candidate[0] < lowest:
                lowest = candidate[0]
                top_idx = t_idx
                nested_idx = n_idx

    if top_idx == None:
        return None, None

    lowest_maps[top_idx][nested_idx][0] = lowest+1
    if lowest_maps[top_idx][nested_idx][0] > lowest_maps[top_idx][nested_idx][1]:
        lowest_maps[top_idx].pop(nested_idx)
    
    return lowest, top_idx


def convert(conversion_map, value):
    result = value
    for connection in conversion_map:
        s_start, s_end = connection["source_start"], connection["source_end"]
        d_start = connection["dest_start"]
        if value >= s_start and value <= s_end:
            diff = value - s_start
            result = d_start + diff
    return result


def deconvert(conversion_maps, idx, value):
    result = value
    for connection in conversion_maps[idx]:
        d_start, d_end = connection["dest_start"], connection["dest_end"]
        s_start = connection["source_start"]
        if value >= d_start and value <= d_end:
            result = value + (s_start - d_start)
            #source = connection["source_start"]
            #for deep_connection in conversion_maps[idx-1]:
            #    dd_start, dd_end = deep_connection["dest_start"], deep_connection["dest_end"]

    return result


def trace_to_end(conversion_maps, idx, value):
    if idx >= 7:
        return value
    
    value = convert(conversion_maps[idx+1], value)
    return trace_to_end(conversion_maps, idx+1, value)


def trace_to_beginning(conversion_maps, idx, value):
    if idx <= 0:
        return value
    

    value = deconvert(conversion_maps, idx-1, value)
    return trace_to_beginning(conversion_maps, idx-1, value)
    

def part_1(data):
    minimum = math.inf
    conversion_maps_list = get_conversion_maps(data)
    seeds = list(map(int, conversion_maps_list[0][0].split(': ')[1].split()))
    
    conversion_maps_list[0] = []

    conversion_maps_list[0].append("seeds map:")
    #for seed in seeds:
    #    conversion_maps_list[0].append(str(seed) + " " + str(seed) + " 1")

    for i in range(0, len(seeds), 2):
        length = seeds[i+1]-seeds[i]+1
        conversion_maps_list[0].append(str(seeds[i]) + " " + str(seeds[i+1]) + " " + str(length))

    conversion_maps = convert_to_dict(conversion_maps_list)
    lowest_table = create_lowest_table(seeds, conversion_maps)


    start, idx = find_lowest(lowest_table)

    for i in range(start, 100000000000000000, 1):
        print(start)
        beg = trace_to_beginning(conversion_maps, 7, start)
        for connection in conversion_maps[0]:
            if beg >= connection["dest_start"] and beg <= connection["source_start"]:
                return start
        start += 1

    # while True:
    #     # Debug

    #     if start == None:
    #         break

    #     end = trace_to_end(conversion_maps, idx, copy.copy(start))

    #     if start == end:
    #         beginning = trace_to_beginning(conversion_maps, idx+1, copy.copy(start))
    #         if beginning in seeds:
    #             return start

    
    

def part_2(data):
    return None
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

# 13 -> 13 -> 52 -> 41 -> 34 -> 34 -> 35 -> -