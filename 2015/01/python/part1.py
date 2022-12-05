floor = 0

instructions = input()

for instr in instructions:
    if instr == '(':
        floor += 1
    elif instr == ')':
        floor -= 1

print(floor)
