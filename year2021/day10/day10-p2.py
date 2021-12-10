import sys

closers = [')', ']', '}', '>']
char_dict = { '(' : ')', '[' : ']', '{' : '}', '<' : '>' }
values = { ')' : 1, ']' : 2, '}' : 3, '>' : 4 }

score = []

for line in sys.stdin:
    expected = []
    line_score = 0
    for c in line:
        if c == '\n':
            expected.reverse()
            for e in expected:
                line_score = line_score * 5 + values[e]
            score.append(line_score)
            break
        if c in closers:
            if c != expected[len(expected)-1]:
                break
            expected.pop()
        else:
            expected.append(char_dict[c])      

score.sort()
middle = int(len(score) / 2)

print(score[middle])