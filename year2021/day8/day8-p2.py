import sys

EIGHT = "abcdefg" 
SEVEN  = "abd" 
SIX = "bcdefg" 
FIVE = "bcdef" 
FOUR = "abef" 
THREE = "abcdf" 
TWO = "acdfg" 
ONE = "ab" 
ZERO = "abcdeg"
#len_to_digit = "00174008"
#decode = { 1 : 0, 4 : 0, 7 : 0, 8 : 0, 0 : 0}

def decode(number):
    if number == ZERO:
        return int(0)
    elif number == ONE:
        return int(1)
    elif number == TWO:
        return int(2)
    elif number == THREE:
        return int(3)
    elif number == FOUR:
        return int(4)
    elif number == FIVE:
        return int(5)
    elif number == SIX:
        return int(6)
    elif number == SEVEN:
        return int(7)
    else:
        return int(8)
    


sum = 0

for line in sys.stdin:
    coded = line.split("| ")[1].split()
    bcd_total = 0
    for i in range(4):
        print(coded[i])
        number = sorted(coded[i])
        number = "".join(number)
        print(number)
        if i == 0:
            decoded = decode(number)
            decoded = decoded * 1000
        elif i == 1:
            decoded = decode(number) * 100
        elif i == 2:
            decoded = decode(number) * 10
        elif i == 3:
            decoded = decode(number)
        bcd_total += decoded
    print(bcd_total)
    print()
    sum += bcd_total

#print(sum)
