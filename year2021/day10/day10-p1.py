import sys

closers = [')', ']', '}', '>']
char_dict = { '(' : ')', '[' : ']', '{' : '}', '<' : '>' }
values = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }

score = 0

for line in sys.stdin:
    line = line.strip()
    expected = []
    for c in line:
        if c in closers:
            if c != expected[len(expected)-1]:
                score += values[c]   
            expected.pop()
        else:
            expected.append(char_dict[c])
      
print(score)