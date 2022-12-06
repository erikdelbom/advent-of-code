from sys import stdin

win = { 'A' : 'B', 'B' : 'C', 'C' : 'A' }
draw = { 'A' : 'A', 'B' : 'B', 'C' : 'C' }
lose = { 'A' : 'C', 'B' : 'A', 'C' : 'B' }
points = { 'A' : 1, 'B' : 2, 'C' : 3 }

score = 0
for line in stdin:
    elf = line.split()[0]
    hand = line.split()[1]
    
    if hand == 'X':
        score += points[lose[elf]]
    elif hand == 'Y':
        score += 3 + points[draw[elf]]
    elif hand == 'Z':
        score += 6 + points[win[elf]]

print(score)