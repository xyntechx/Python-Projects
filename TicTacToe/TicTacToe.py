def play(move, board, char):
    board[move-1] += [char]
    return board

def show_board(board):
    print(f"{str(board[0]):<5}{str(board[1]):^5}{str(board[2]):>5}")
    print(f"{str(board[3]):<5}{str(board[4]):^5}{str(board[5]):>5}")
    print(f"{str(board[6]):<5}{str(board[7]):^5}{str(board[8]):>5}")

def empty(board):
    is_empty = False
    for box in board:
        if len(box) == 0:
            is_empty = True
            break
    return is_empty

def finished(board, char):
    is_finished = False   
    if (char in board[0] and char in board[3] and char in board[6]) or (char in board[1] and char in board[4] and char in board[7]) or (char in board[2] and char in board[5] and char in board[8]) or (char in board[0] and char in board[1] and char in board[2]) or (char in board[3] and char in board[4] and char in board[5]) or (char in board[6] and char in board[7] and char in board[8]) or (char in board[0] and char in board[4] and char in board[8]) or (char in board[2] and char in board[4] and char in board[6]):
        is_finished = True
    return [is_finished, char]

board = [[], [], [], [], [], [], [], [], []]

print("Refer to the board below for the boxes' numbers while you play!")
print("[1] [2] [3]")
print("[4] [5] [6]")
print("[7] [8] [9]")
print()
print("How To Play:")
print("When prompted, type in either 'X' or 'O' followed by a box's number to occupy the box using either 'X' or 'O'.")
print("For example, if 'X1' is typed in, 'X' appears in the top left box labelled '1'.")

while empty(board):
    move = input()
    board = play(int(move[1]), board, move[0])
    show_board(board)
    if finished(board, move[0])[0]:
        print("Game Over! The winner is '" + finished(board, move[0])[1] + "'!")
        break

if not empty(board):
    print("Game Over! It's a tie!")