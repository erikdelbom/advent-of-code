import shapely
from shapely.geometry import LineString, Point

def read_input():
    with open('data.in', 'r') as f:
        data = {}
        for line in f.readlines():
            sensor, beacon = line.split(': ')
            sensor_x, sensor_y = sensor.split(',')
            beacon_x, beacon_y = beacon.split(',')
            
            sensor_x = int(sensor_x[sensor_x.find('=')+1:])
            sensor_y = int(sensor_y[sensor_y.find('=')+1:])
            beacon_x = int(beacon_x[beacon_x.find('=')+1:])
            beacon_y = int(beacon_y[beacon_y.find('=')+1:])
            data[(sensor_x, sensor_y)] = (beacon_x, beacon_y)
    
    return data

def manhattan(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def part_1(data):
    row = 2_000_000
    points = set()
    for sensor in data.keys(): 
        beacon = data[sensor]
        left_x = sensor[0] - manhattan(sensor, beacon)
        right_x = sensor[0] + manhattan(sensor, beacon)
        steps = abs(sensor[1] - row)

        left_x += steps
        right_x -= steps

        if left_x < right_x:
            for i in range(left_x, right_x+1, 1):
                points.add(i)
    
    beacons_on_row = set()
    for beacon in data.values():
        if beacon[1] == row:
            beacons_on_row.add(beacon[0])

    for i in points & beacons_on_row:
        points.remove(i)

    return len(points)

def get_mid_point(p1, p2, p3, p4):
    x_values = [p1[0], p2[0], p3[0], p4[0]]
    y_values = [p1[1], p2[1], p3[1], p4[1]]
    x = max(set(x_values), key=x_values.count)
    y = max(set(y_values), key=y_values.count)

    return (x, y)


def part_2(data):
    lim = 4_000_000
    lines_up = []
    lines_down = []
    for key in data.keys():
        length = manhattan(key, data[key])
        
        l1 = LineString([(key[0]-length, key[1]), (key[0], key[1]-length)])
        l2 = LineString([(key[0], key[1]+length), (key[0]+length, key[1])])
        l3 = LineString([(key[0], key[1]-length), (key[0]+length, key[1])])
        l4 = LineString([(key[0]-length, key[1]), (key[0], key[1]+length)])

        lines_up.append(l1)
        lines_up.append(l2)

        lines_down.append(l3)
        lines_down.append(l4)

    intersections = set()
    for l1 in lines_up:
        for l2 in lines_down:
            int_pt = l1.intersection(l2)
            if int_pt:
                intersections.add((int_pt.x, int_pt.y))

    for i1 in intersections:
        for i2 in intersections:
            if manhattan(i1, i2) == 2:
                for i3 in intersections:
                    if ( manhattan(i1, i3) == 2 
                         and manhattan(i2, i3) == 2 ):
                        for i4 in intersections:
                            if ( manhattan(i1, i4) == 2 
                                and manhattan(i3, i4) == 2 
                                and manhattan(i2, i4) == 2 ):
                                    pt = get_mid_point(i1, i2, i3, i4)
                                    if ( (pt[0] >= 0 and pt[0] <= lim ) 
                                        and (pt[1] >= 0 and pt[1] <= lim) ):
                                            return int(pt[0]*lim + pt[1])                                        

print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))