import sys

DAYS_IN_CYCLE = 9
DAY_AFTER_RE = 6
TOTAL_DAYS = 256

def cycle(days):
    new_fishes = days[0]
    for i in range(DAYS_IN_CYCLE-1):
        days[i] = days[i+1]
    days[DAYS_IN_CYCLE-1] = new_fishes
    days[DAY_AFTER_RE] += new_fishes

for line in sys.stdin:
    fishes = line.split(',')
fishes = [int(i) for i in fishes]

days = [0] * DAYS_IN_CYCLE
total = 0

for fish in fishes:
    days[fish] += 1

for i in range(TOTAL_DAYS):
    cycle(days)

total += sum(days)
days = [0] * DAYS_IN_CYCLE

print(total)