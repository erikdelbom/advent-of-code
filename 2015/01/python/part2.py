floor = 0

instructions = input()

for idx, instr in enumerate(instructions):
    if instr == '(':
        floor += 1
    elif instr == ')':
        floor -= 1
    
    if floor < 0:
        print(idx+1)
        break
