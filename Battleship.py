from random import randint

def place_ships(board):
    i=0
    while i < 3:
        i+=1
        col=randint(0,3)
        row=randint(0,2)
        if board[row][col]=="X":
            continue
        elif col==0 and row==0:
            if board[col][row+1]=="X" or board[col+1][row]=="X" or board[col+1][row+1]=="X":
                continue
        elif col==0 and row==1:
            if board[col][row+1]=="X" or board[col+1][row]=="X" or board[col+1][row+1]=="X":
                continue


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
    return row, col

def hit_or_miss(row, col):
        if board[row][col] !="-":
            print("You sunk my battleship")
            board[row][col]="-"
        else:
            print=("You missed")

def victory(board, count_shots):
    if "X" not in board:
        print("You hit all the ships in {} attempts".format(count_shots))






count_shots=0
board=board=[[ "-", "-", "-", "-" ], ["-", "-", "-", "-"], ["-", "-", "-", "-"]]
