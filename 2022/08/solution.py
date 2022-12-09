def read_input():
    with open('data.in', 'r') as f:
        lines = []
        for l in f:
            li = []
            for c in l.strip():
                li.append(int(c))
            lines.append(li)
        return lines

def part_1(data):
    width = len(data[0])
    height = len(data)
    sum = 2*height + 2*width - 4 

    for row in range(1, height-1): 
        for col in range(1, width-1): 
            cur = data[row][col]
            reach = False

            # Look north
            for n in range(1, row+1):
                if cur <= data[row-n][col]:
                    break
                if row-n == 0:
                    reach = True
            
            if reach:
                sum += 1
                continue
            
            # Look east
            for n in range(1, width-col):
                if cur <= data[row][col+n]:
                    break
                if col+n == width-1:
                    reach = True

            if reach:
                sum += 1
                continue
                    
            # Look south
            for n in range(1, height-row):
                if cur <= data[row+n][col]:
                    break
                if row+n == height-1:
                    reach = True

            if reach:
                sum += 1
                continue
            
            # Look west
            for n in range(1, col+1):
                if cur <= data[row][col-n]:
                    break
                if col-n == 0:
                    reach = True

            if reach:
                sum += 1
                continue
    
    return sum

def part_2(data):
    width = len(data[0])
    height = len(data)
    highest_score = 0

    for row in range(1, height-1): 
        for col in range(1, width-1): 
            cur = data[row][col]
            print()
            print("cur:", cur)

            # Look north
            north = 0
            for n in range(1, row+1):
                if cur <= data[row-n][col]:
                    north += 1
                    break
                north += 1
            print("north:", north)

            # Look east
            east = 0
            for n in range(1, width-col):
                if cur <= data[row][col+n]:
                    east += 1
                    break
                east += 1
            print("east:", east)
           
            # Look south
            south = 0
            for n in range(1, height-row):
                if cur <= data[row+n][col]:
                    south += 1
                    break
                south += 1
            print("south:", south)

            # Look west
            west = 0
            for n in range(1, col+1):
                if cur <= data[row][col-n]:
                    west += 1
                    break
                west += 1
            print("west:", west)
        
            score = north * east * south * west
            print(score)


            if score > highest_score:
                highest_score = score
    
    return highest_score

print("Part 1:", part_1(read_input()))
print("Part 2:", part_2(read_input()))