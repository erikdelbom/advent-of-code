import sys

row_length = 0
octos = []

for line in sys.stdin:
    line = line.strip()
    row_length = len(line)
    for c in line:
        octos.append(int(c))

print(row_length)
for i in range(len(octos)):
    if i % row_length == 0:
       print()
    print(octos[i], end='')

#print(octos)