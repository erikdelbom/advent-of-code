import sys
import time

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


def calculate_distance(hold_time, total_time):
    travel_time = total_time - hold_time
    velocity = hold_time

    return velocity*travel_time

def part_1(data):
    time = []
    record = []
    distances = []

    for t in data[0].split()[1:]:
        time.append(int(t))
    for r in data[1].split()[1:]:
        record.append(int(r))

    
    for t in time:
        tmp_distances = []
        for i in range(t+1):
            tmp_distances.append(calculate_distance(i, t))
        distances.append(tmp_distances)


    product = 1
    for idx, r in enumerate(record):
        count = 0
        for dist in distances[idx]:
            if dist > r:
                count += 1
        product *= count

    return product
def part_2(data):
    time = ""
    record = ""
    distances = []

    for t in data[0].split()[1:]:
        time += t
    for r in data[1].split()[1:]:
        record += r

    time = int(time)
    record = int(record)

    print(time)
    print(record)
    
    count = 0
    for i in range(time):
        distance = calculate_distance(i, time)
        if distance > record:
            count += 1

    return count

    # for t in time:
    #     tmp_distances = []
    #     for i in range(t+1):
    #         tmp_distances.append(calculate_distance(i, t))
    #     distances.append(tmp_distances)


    # product = 1
    # for idx, r in enumerate(record):
    #     count = 0
    #     for dist in distances[idx]:
    #         if dist > r:
    #             count += 1
    #     product *= count

    # return product


input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")