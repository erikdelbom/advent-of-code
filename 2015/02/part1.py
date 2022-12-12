from sys import stdin

total = 0

for line in stdin:
    l, w, h = map(int, line.split('x'))
    total += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

print(total)