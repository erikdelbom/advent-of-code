import sys
import time
import re
import math

def read_input(filename):
    with open(filename, 'r') as f:
        return list(map(str.rstrip, f.readlines()))

def gcdExtended(a, b): 
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 

def part_1(data):
    for i in range(0, len(data), 4):
        ax = int(re.search(r"X\+[0-9]+", data[i]).group().split('+')[1])
        ay = int(re.search(r"Y\+[0-9]+", data[i]).group().split('+')[1])
        bx = int(re.search(r"X\+[0-9]+", data[i+1]).group().split('+')[1])
        by = int(re.search(r"Y\+[0-9]+", data[i+1]).group().split('+')[1])
        cx = int(re.search(r"X\=[0-9]+", data[i+2]).group().split('=')[1])
        cy = int(re.search(r"Y\=[0-9]+", data[i+2]).group().split('=')[1])
        
        gcdx, a, b = gcdExtended(ax, bx)
        if cx % gcdx != 0:
            continue
        print(gcdx, a, b, cx)
        print(a * (cx // gcdx), b * (cx // gcdx)) 


def part_2(data):
    return None

input_file = sys.argv[1]

start_time = time.time()
print("Part 1:", part_1(read_input(input_file)), end=" - ") 
print(round((time.time() - start_time), 3), "s")

start_time = time.time()
print("Part 2:", part_2(read_input(input_file)), end=" - ")
print(round((time.time() - start_time), 3), "s")
