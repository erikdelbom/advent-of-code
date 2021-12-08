import sys

len_to_digit = "00174008"
digit_count = { 1 : 0, 4 : 0, 7 : 0, 8 : 0, 0 : 0}

for line in sys.stdin:
    line = line.split("| ")[1].split()
    for l in line:
        digit_count[int(len_to_digit[len(l)])] += 1

sum = 0

for d in digit_count:
    if d != 0:
        sum += digit_count[d]

print(sum)