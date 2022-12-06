from sys import stdin

sum = 0

for l in stdin:
    pair = l.strip().split(',')
    left_lower, left_upper = map(int, pair[0].split('-'))
    right_lower, right_upper = map(int, pair[1].split('-'))
    left = set(range(left_lower, left_upper+1))
    right = set(range(right_lower, right_upper+1))

    if left.intersection(right):
        sum += 1

print(sum)
