from random import randint

def place_ships(board):
    i=0
    while i < 3:
        col=randint(0,3)
        row=randint(0,2)
        if board[row][col]=="X":
            continue
        if col>0 and board[row][col-1]=="X":
            continue
        if col<3 and board[row][col+1]=="X":
            continue
        if row>0 and board[row-1][col]=="X":
            continue
        if row<2 and board[row+1][col]=="X":
            continue
        else:
            i+=1
            board[row][col]="X"

def getRowCol(count_shots):
    count_shots+=1
    while True:
        col=input("Enter a column: ").upper()
        row=int(input("Enter a row: "))-1
        if row>3 or row<0 or col>"D" or col<"A":
            print("This is not a position on the board.")
            continue
        else:
            col=ord(col)-ord("A")
            break
    return row, col, count_shots

def hit_or_miss(row, col):
        if board[row][col] !="-":
            print("You sunk my battleship")
            board[row][col]="-"
        else:
            print("You missed")

def victory(board, count_shots):
    if "X" not in board[0] and "X" not in board[1] and "X" not in board[2]:
        print("You hit all the ships in {} attempts".format(count_shots))
        return True

count_shots=0
board=[[ "-", "-", "-", "-" ], ["-", "-", "-", "-"], ["-", "-", "-", "-"]]

place_ships(board)
print(board)
while True:
    row, col, count_shots = getRowCol(count_shots)
    hit_or_miss(row, col)
    if victory(board, count_shots):
        break
