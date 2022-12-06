from sys import stdin

win = { 'A' : 'Y', 'B' : 'Z', 'C' : 'X' }
draw = { 'X' : 'A', 'Y' : 'B', 'Z' : 'C' }
points = { 'X' : 1, 'Y' : 2, 'Z' : 3 }

score = 0
for line in stdin:
    elf = line.split()[0]
    hand = line.split()[1]

    if win[elf] == hand:
        score += (6 + points[hand])
    elif elf == draw[hand]:
        score += (3 + points[hand])
    else:
        score += points[hand]

print(score)
