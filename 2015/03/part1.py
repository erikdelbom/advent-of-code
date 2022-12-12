data = input()
houses = { (0, 0) : 1 }
x_dir = { '>' : 1, 'v' : 0, '<' : -1, '^' : 0} 
y_dir = { '>' : 0, 'v' : -1, '<' : 0, '^' : 1} 
x = 0
y = 0

sum = 1

for c in data:
    x += x_dir[c]
    y += y_dir[c]
    if (x, y) not in houses:
        houses[(x, y)] = 1
        sum += 1

print(houses)
print(sum)