
def read_input():
    with open('data.in', 'r') as f:
        return list(map(str.rstrip, f.readlines()))

table = { "one" : 1, "two" : 2, "three" : 3, 
          "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

def part_1(inp):
    sum = 0
    for i in inp:
        num = ""
        word = ""
        for c in i:
            if c.isnumeric():
                num += c
            elif c.isalpha():
                word += c

            for key in table.keys():
                if key in word:
                    num += str(table[key])
                    word = word[-1]
        
        print(i)
        print(num[0]+num[-1])
        print()
        sum += int(num[0]+num[-1])


    return sum

print("Part 1:", part_1(read_input()))
#print("Part 2:", part_2(read_input()))