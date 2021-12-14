import sys

def remove_duplicates(lst):
    dots.sort()
    i = 0
    while i < len(lst)-1:
        if lst[i][0] == lst[i+1][0]:
            if lst[i][1] == lst[i+1][1]:
                lst.pop(i)
        i += 1

dots = []

for line in sys.stdin:
    if line == '\n': break
    x, y = line.strip().split(',')
    dot = [int(x), int(y)]
    dots.append(dot)

instructions = []

for line in sys.stdin:
    instruction = line.strip().split('=')
    instruction = (instruction[0][len(instruction[0])-1], int(instruction[1]))
    instructions.append(instruction)

instr = instructions[0]
if instr[0] == 'x':
    for d in dots:
        if d[0] > instr[1]:
            new_x = instr[1] - abs(d[0] - instr[1])
            d[0] = new_x
elif instr[0] == 'y':
    for d in dots:
        if d[1] > instr[1]:
            new_y = instr[1] - abs(d[1] - instr[1])
            d[1] = new_y

remove_duplicates(dots)

print(len(dots)) 