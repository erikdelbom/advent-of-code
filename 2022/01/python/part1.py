from sys import stdin

elfs = []
tmp = 0

for l in stdin:
    if l == '\n':
        elfs.append(tmp)
        tmp = 0
        continue
    tmp += int(l)

print(max(elfs))