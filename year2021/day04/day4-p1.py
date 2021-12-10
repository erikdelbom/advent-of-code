import sys

class Bingo_Board():
    def __init__(self, list):
        self.data = list
        self.bingo_check =  [[0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0]]
        self.turns = 0
        self.winning_number = 0;

    def bingo(self):
        for row in self.bingo_check:
            if sum(row, 0) == 5:
                return True
        
        columns = [0, 0, 0, 0, 0]
        for row in self.bingo_check:
            for i in range(5):
                columns[i] += row[i]
        
        for c in columns:
            if c == 5:
                return True

        return False

    def count_turns(self, bingo_numbers):
        count = 0
        check = self.bingo_check
        for i in bingo_numbers:
            for j in range(5):
                for k in range(5):
                    if self.data[j][k] == i:
                        check[j][k] = 1
            count += 1
            if self.bingo():
                self.turns = count
                self.winning_number = i
                return

    def sum(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                if self.bingo_check[i][j] == 0:
                    sum += self.data[i][j]
        return sum
                
    # Member variables 
    data = []
    bingo_check =  []
    turns = 0
    winning_number = 0


bingo_numbers = input().split(",")
bingo_numbers = [int(i) for i in bingo_numbers]

bingo_boards = []
bingo_board = []
input()

for line in sys.stdin:
    if line == '\n':
        bingo_boards.append(Bingo_Board(bingo_board))
        bingo_board = []
    else:
        row = line.split()
        row = [int(i) for i in row]
        bingo_board.append(row)
bingo_boards.append(Bingo_Board(bingo_board))

for i in range(len(bingo_boards)):
    bingo_boards[i].count_turns(bingo_numbers)

bingo_boards.sort(key=lambda bingo_board: bingo_board.turns)

print(bingo_boards[0].winning_number * bingo_boards[0].sum())