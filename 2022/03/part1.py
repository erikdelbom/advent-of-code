from sys import stdin

items = []

for l in stdin:
    firsthalf = l[:len(l)//2]
    secondhalf = l[len(l)//2:]

    done = False
    for c in firsthalf:
        if done:
            break
        for p in secondhalf:
            if c == p:
                print(c)
                done = True
                prio = 1
                if c.isupper():
                    prio = 27 + (ord(c) - 0x41)
                elif c.islower():
                    prio = 1 + (ord(c) - 0x61)
                items.append(prio)
                break

print(sum(items))