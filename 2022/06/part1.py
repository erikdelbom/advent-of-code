from sys import stdin

l = input()
n = 4

for idx, c in enumerate(l):
    s = set()
    for i in range(n):
        s.add(l[idx+i])
    if len(s) == n:
        print(idx+n)
        break
