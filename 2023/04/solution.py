import re
import sys

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))


def part_1(data):
    sum = 0
    for line in data:
        numbers, winners = line.split(': ')[1].split(' | ')
        numbers, winners = numbers.replace('  ', ' ').split(), winners.replace('  ', ' ').split()
        
        numbers, winners = set(map(int, numbers)), set(map(int, winners))
        res = int(2**(len(numbers & winners)-1))
        sum += res 

    return sum

def part_2(data):
    sum = 0
    cards = []
    done = False
    for line in data:
        numbers, winners = line.split(': ')[1].split(' | ')
        numbers, winners = numbers.replace('  ', ' ').split(), winners.replace('  ', ' ').split()
        numbers, winners = set(map(int, numbers)), set(map(int, winners))
        wins = len(numbers & winners)
        cards.append([1, wins])

    prev_sum = sum
    while True:
        for i in range(len(cards)):
            if cards[i][0] > 0:
                sum += 1
                cards[i][0] -= 1
                for j in range(cards[i][1]):
                    cards[i+j+1][0] += 1
        if sum == prev_sum:
            break
        prev_sum = sum 

    return sum


input_file = sys.argv[1]

print("Part 1:", part_1(read_input(input_file)))
print("Part 2:", part_2(read_input(input_file)))