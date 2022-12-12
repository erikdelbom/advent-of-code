from sys import stdin

total = 0

for line in stdin:
    l, w, h = map(int, line.split('x'))
    total += min(2*(l+w), 2*(w+h),2*(h+l)) + l*w*h

print(total)