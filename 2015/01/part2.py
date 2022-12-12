data = input()
floor = 0

for idx, c in enumerate(data):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1

    if floor == -1:
        print(idx+1)
        break

