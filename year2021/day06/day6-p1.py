import sys

for line in sys.stdin:
    fishes = line.split(',')
fishes = [int(i) for i in fishes]

for i in range(80):
    for j in range(len(fishes)):
        if fishes[j] == 0:
            fishes[j] = 6
            fishes.append(8)
        else:
            fishes[j] -= 1

print(len(fishes))