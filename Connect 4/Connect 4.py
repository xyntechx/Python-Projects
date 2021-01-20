# CLASSES
class Colour:
    BOLD = "\033[1m"
    END = "\033[0m"


class Player:
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname.upper()
    
    def get_name(self):
        return self.name
    
    def get_nickname(self):
        return self.nickname



# FUNCTIONS
def update_board(board, player):
    '''
    Updates the board after a move
    '''
    column_num = (int(input(Colour.BOLD + player.get_name() + "'s column choice [1/2/3/4/5/6/7]: " + Colour.END)) - 1)*2 + 1
    row_num = 5

    for row in board[::-1]:
        if row[column_num] == "O":
            board[row_num] = board[row_num][:column_num] + player.get_nickname() + board[row_num][column_num+1:]
            break
        row_num -= 1
    
    return board

def check_horizontal(board, char):
    '''
    Checks whether or not a 4-in-a-row occurs horizontally
    '''
    for row_num in range(6):
        for column_num in range(7, 15, 2):
            if board[row_num][column_num] == char and board[row_num][column_num-2] == char and board[row_num][column_num-4] == char and board[row_num][column_num-6] == char:
                return True
    return False

def check_vertical(board, char):
    '''
    Checks whether or not a 4-in-a-row occurs vertically
    '''
    for column_num in range(1, 15, 2):
        for row_num in range(3, len(board)):
            if board[row_num][column_num] == char and board[row_num-1][column_num] == char and board[row_num-2][column_num] == char and board[row_num-3][column_num] == char:
                return True
    return False

def check_diagonal(board, char, direction):
    '''
    Checks whether or not a 4-in-a-row occurs diagonally
    '''
    if direction == "RIGHT":
        board = board[::-1]

    for i in range(3):
        if i == 0:
            row_start, row_end = 0, 4
        elif i == 1:
            row_start, row_end = 1, 5
        elif i == 2:
            row_start, row_end = 2, 6

        slope1, slope2, slope3, slope4 = 0, 0, 0, 0
        for row_num in range(row_start, row_end):
            if row_num == row_start:
                start, stop = 1, 8
            elif row_num == row_start + 1:
                start, stop = 3, 10
            elif row_num == row_start + 2:
                start, stop = 5, 12
            elif row_num == row_start + 3:
                start, stop = 7, 14

            for column_num in range(start, stop, 2):
                if column_num == start:
                    if board[row_num][column_num] == char:
                        slope1 += 1
                elif column_num == start + 2:
                    if board[row_num][column_num] == char:
                        slope2 += 1
                elif column_num == start + 4:
                    if board[row_num][column_num] == char:
                        slope3 += 1
                elif column_num == start + 6:
                    if board[row_num][column_num] == char:
                        slope4 += 1
        
        if slope1 >= 4 or slope2 >= 4 or slope3 >= 4 or slope4 >= 4:
            return True
    return False

def finished(board, player):
    '''
    Checks whether or not a player has won, i.e. the game is finished
    '''
    char = player.get_nickname()

    horizontal_win = check_horizontal(board, char)
    vertical_win = check_vertical(board, char)
    diagonal_left_win = check_diagonal(board, char, "LEFT")
    diagonal_right_win = check_diagonal(board, char, "RIGHT")
    
    if horizontal_win or vertical_win or diagonal_left_win or diagonal_right_win:
        return True
    return False



# INITIALISATION
board = []
for _ in range(6):
    row = ""
    for _ in range(7):
        row += "|O"
    board.append(row + "|")

player_a = Player(input("Player A's Name: "), "A")
player_b = Player(input("Player B's Name: "), "B")
print()

print(Colour.BOLD + "|1|2|3|4|5|6|7|" + Colour.END)
print("\n".join(board) + "\n")

count = 1



# GAME
while True:
    if count & 1:
        board = update_board(board, player_a)
    else:
        board = update_board(board, player_b)

    print(Colour.BOLD + "|1|2|3|4|5|6|7|" + Colour.END)
    print("\n".join(board) + "\n")

    filled_row_count = 0
    for row in board:
        if not row.count("O"):
            filled_row_count += 1

    if finished(board, player_a) or finished(board, player_b) or filled_row_count == 6:
        break
    
    count += 1

if finished(board, player_a):
    print(Colour.BOLD + player_a.get_name() + " wins!" + Colour.END)
elif finished(board, player_b):
    print(Colour.BOLD + player_b.get_name() + " wins!" + Colour.END)

input(Colour.BOLD + "Press Enter to quit..." + Colour.END)