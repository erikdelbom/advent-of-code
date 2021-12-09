import sys

height_map = []
row_length = 0

for line in sys.stdin:
    row_length = len(line)-1
    for c in line:
        if c != '\n':
            height_map.append(int(c))

right_col = row_length-1

sum = 0


for i in range(len(height_map)):
    # Upper row
    if i < row_length:
        # Upper left corner
        if i % row_length == 0:
            if height_map[i] < height_map[i+1] and height_map[i] < height_map[i+row_length]:
                sum += height_map[i]+1
        # Upper right corner
        elif i % (right_col) == 0:
            if height_map[i] < height_map[i-1] and height_map[i] < height_map[i+row_length]:
                sum += height_map[i]+1
            right_col += row_length
        else:
            if height_map[i] < height_map[i-1] and height_map[i] < height_map[i+row_length] and height_map[i] < height_map[i+1]:
                sum += (height_map[i]+1)
            

    # Bottom row
    elif i >= (len(height_map) - row_length):
        # Bottom left corner
        if i % (row_length) == 0:
            if height_map[i] < height_map[i+1] and height_map[i] < height_map[i-row_length]:
                sum += height_map[i]+1
        # Bottom right corner
        elif i % (right_col) == 0:
            if height_map[i] < height_map[i-1] and height_map[i] < height_map[i-row_length]:
                sum += height_map[i]+1
            right_col += row_length
        else:
            if height_map[i] < height_map[i+1] and height_map[i] < height_map[i-row_length] and height_map[i] < height_map[i-1]:
                sum += height_map[i]+1
    
    # Left column
    elif i % row_length == 0:
        if height_map[i] < height_map[i+1] and height_map[i] < height_map[i+row_length] and height_map[i] < height_map[i-row_length]:
                sum += height_map[i]+1     
    
    # Right Column
    elif i % right_col == 0:
        if height_map[i] < height_map[i-1] and height_map[i] < height_map[i+row_length] and height_map[i] < height_map[i-row_length]:
                sum += height_map[i]+1
        right_col += row_length
    
    else:
        if height_map[i] < height_map[i+1] and height_map[i] < height_map[i+row_length] and height_map[i] < height_map[i-row_length] and height_map[i] < height_map[i-1]:
                sum += (height_map[i]+1)
print(sum)



    