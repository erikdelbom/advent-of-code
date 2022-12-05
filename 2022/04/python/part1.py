from sys import stdin

stacks = []
for l in stdin:
    if l == '\n':
        break
    crates = [l[i:i+4].strip() for i in range(0, len(l), 4)]

    print(crates)

    for idx, c in enumerate(crates):
        crates[idx] = c[1:2]
    #print(crates)

    for idx, c in enumerate(crates):
        if idx > len(stacks)-1:
            stacks.append([])
        if c != '':
            stacks[idx].insert(0,c)

print(stacks)

for l in stdin:
    num = int(l.split('move ')[1].split(' from')[0])
    fr = int(l.split('from ')[1].split(' to')[0])-1
    to = int(l.split('to ')[1])-1

    for n in range(num):
        tmp = stacks[fr].pop()
        stacks[to].append(tmp)

print(stacks)
for s in stacks:
    print(s[-1],end='')
print()