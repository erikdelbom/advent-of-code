class Bingo_Board():
    def __init__():
        data = [[]]
    
    def bingo(self):
        for row in self.data:
            if sum(row, 0) == -5:
                return True
        
        columns = [0, 0, 0, 0, 0]
        for row in self.data:
            for i in range(5):
                columns[i] += row[i]
        
        for c in columns:
            if c == -5:
                return True

        return False

    def count_turns(self, bingo_numbers):
        count = 0
        for i in bingo_numbers:
            for row in self.data:
                for elem in row:
                    if elem == i:
                        elem = -1
            count += 1
            if self.bingo():
                self.turns = count



    data = []
    turns = 0


bingo_numbers = input().split(",")
bingo_numbers = [int(i) for i in bingo_numbers]

bingo_boards = []
input()
tmp = Bingo_Board

for i in range(5):
    row = input().split()
    row = [int(j) for j in row]
    tmp.data.append(row)


for i in tmp:
    print(i)


