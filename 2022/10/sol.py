from sys import stdin

reg_x = 1
cycle = 1
sum = 0
vals = {}

for line in stdin:
    print(len(line.split()))
    if len(line.split()) == 2:
        op, arg = line.split()
        for i in range(2):
            vals[cycle] = cycle * reg_x
            cycle += 1 
        reg_x += int(arg)
    else:
        vals[cycle] = cycle * reg_x
        cycle += 1


print(vals[20] + vals[60] + vals[100] + vals[140] + vals[180] + vals[220])
# print(vals[20])
# print(vals[60])
# print(vals[100])
# print(vals[140])
# print(vals[180])
# print(vals[219])
