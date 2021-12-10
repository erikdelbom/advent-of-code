crab_positions = input().split(',')
crab_positions = [int(i) for i in crab_positions]
crab_dict = {}

for i in crab_positions:
    crab_dict[i] = 0

for i in crab_positions:
    crab_dict[i] += 1

all_positions = [i for i in range(max(crab_positions))]
all_fuel = []

for curr_pos in all_positions:
    fuel = 0
    for key in crab_dict:
        distance = abs(key - curr_pos) 
        distance = ((distance**2 + distance) / 2) * crab_dict[key]
        fuel += distance
    all_fuel.append(fuel)

print(int(min(all_fuel)))