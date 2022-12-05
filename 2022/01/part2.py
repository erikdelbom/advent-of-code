from sys import stdin

elfs = []
tmp = 0

for l in stdin:
    if l == '\n':
        elfs.append(tmp)
        tmp = 0
        continue
    tmp += int(l)

elfs.sort(reverse=True)
m = elfs[0] + elfs[1] + elfs[2]

print(m)