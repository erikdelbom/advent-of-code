data = input()
houses = { (0, 0) : 1 }
x_dir = { '>' : 1, 'v' : 0, '<' : -1, '^' : 0} 
y_dir = { '>' : 0, 'v' : -1, '<' : 0, '^' : 1} 
santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0

sum = 1

for turn, c in enumerate(data):
    x = 0
    y = 0
    if turn % 2 == 0:
        santa_x += x_dir[c]
        santa_y += y_dir[c]
        x = santa_x
        y = santa_y
    else:
        robo_x += x_dir[c]
        robo_y += y_dir[c]
        x = robo_x
        y = robo_y
    if (x, y) not in houses:
        houses[(x, y)] = 1
        sum += 1

print(sum)