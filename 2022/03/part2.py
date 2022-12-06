from sys import stdin

items = []
group = []
count = 0
for l in stdin:
    group.append(l)
    count += 1

    if count < 3:
        continue

    done = False
    for c in group[0]:
        if done:
            break
        for p in group[1]:
            if c == p:
                for q in group[2]:
                    if q == c:
                        done = True
                        prio = 1
                        if c.isupper():
                            prio = 27 + (ord(c) - 0x41)
                        elif c.islower():
                            prio = 1 + (ord(c) - 0x61)
                        items.append(prio)
                        break
                break
    
    group = []
    count = 0

print(sum(items))