
def display_board(board):
    for i in board:
        print(i)

def getRowCol():
    while True:
        row=int(input("Enter a row: "))-1
        col=int(input("Enter a column: "))-1
        if row>2 or row<0 or col>2 or col<0:
            print("This is not a position on the board.")
            continue
        elif board[row][col] !="-":
            print("This place is already occupied.")
            continue
        else:
            break
    return row, col

def switch_player(player):
    if player =="X":
        player="O"
        return player
    else:
        player="X"
        return player

def winner(board):
    if board[0] == 3*["X"] or board[1] == 3*["X"] or board[2] == 3*["X"]:
        return "X"
    elif board[0] == 3*["O"] or board[1] == 3*["O"] or board[2] == 3*["O"]:
        return "O"
    elif (board[0][0]=="X" and board[1][0] =="X" and board[2][0] =="X") or (board[0][1]=="X" and board[1][1] =="X" and board[2][1] =="X") or (board[0][2]=="X" and board[1][2] =="X" and board[2][2] =="X"):
        return "X"
    elif (board[0][0]=="O" and board[1][0] =="0" and board[2][0] =="0") or (board[0][1]=="0" and board[1][1] =="0" and board[2][1] =="0") or (board[0][2]=="0" and board[1][2] =="0" and board[2][2] =="0"):
        return "0"
    elif (board[0][0]=="X" and board[1][1] =="X" and board[2][2] =="X") or (board[0][2]=="X" and board[1][1] =="X" and board[2][0] =="X"):
        return "X"
    elif (board[0][0]=="0" and board[1][1] =="0" and board[2][2] =="0") or (board[0][2]=="0" and board[1][1] =="0" and board[2][0] =="0"):
        return "0"
    else:
        return

def draw(board):
    if "-" not in board:
        return 
    else:
        return

player="X"
board=[[ "-", "-", "-" ], ["-", "-", "-"], ["-", "-", "-"]]

while True:
    display_board(board)
    r, c = getRowCol()
    board[r][c] = player
    if winner(board):
        print(winner(board), "is the winner.")
        break
    elif draw(board):
        print("Draw")
        break
    else:
        player = switch_player(player)
