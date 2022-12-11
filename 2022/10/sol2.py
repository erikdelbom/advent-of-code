from sys import stdin

reg_x = 1
cycle = 1
sum = 0
cur_px = 0
vals = {}

for line in stdin:
    if len(line.split()) == 2:
        op, arg = line.split()
        for i in range(2):
            if cur_px >= reg_x-1 and cur_px <= reg_x+1:
                print('#',end='')
            else:
                print('.',end='')
            cur_px += 1
            if cycle % 40 == 0:
                cur_px = 0
                print()
            cycle += 1 
        reg_x += int(arg)
    else:
        if cur_px >= reg_x-1 and cur_px <= reg_x+1:
            print('#',end='')
        else:
            print('.',end='')
        cur_px += 1
        
        if cycle % 40 == 0:
            print()
            cur_px = 0
        
        cycle += 1



