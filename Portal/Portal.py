from random import randint


# C L A S S E S
class Color:
    CYAN = "\033[96m"
    RED = "\033[91m"
    END = "\033[0m"


class Player:
    def __init__(self, name, position, colour):
        if colour == "CYAN":
            self.avatar = Color.CYAN + "[O]" + Color.END
        else:
            self.avatar = Color.RED + "[O]" + Color.END
        self.name = name
        self.position = position

    def get_avatar(self):
        return self.avatar

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position
    
    def set_position(self, moves = 0, portal_position = 0):
        if moves:
            if self.position[0] + moves > 9:
                if self.position[1] == 9:
                    self.position[0] += moves
                else:
                    moves -= 10 - self.position[0]
                    self.position[0] = moves
                    self.position[1] += 1
            else:
                self.position[0] += moves
        elif portal_position:
            self.position[0] = portal_position[0]
            self.position[1] = portal_position[1]


# F U N C T I O N S
def update_board():
    x1, y1 = player1_position[0], player1_position[1]
    x2, y2 = player2_position[0], player2_position[1]
    new_board = board[:]
    if x1 >= 9 and y1 >= 9:
        new_board[0] = new_board[0][:-3] + player1.get_avatar()
    elif x2 >= 9 and y2 >= 9:
        new_board[0] = new_board[0][:-3] + player1.get_avatar()
    else:
        if x1 == x2 and y1 == y2:
            new_board[9 - y1] = new_board[9 - y1][:x1*3] + player1.get_avatar() + new_board[9 - y1][x1*3 + 3:]
        else:
            new_board[9 - y1] = new_board[9 - y1][:x1*3] + player1.get_avatar() + new_board[9 - y1][x1*3 + 3:]
            new_board[9 - y2] = new_board[9 - y2][:x2*3] + player2.get_avatar() + new_board[9 - y2][x2*3 + 3:]
    return new_board

def game_on(player):
    player_position = player.get_position()
    x, y = player_position[0], player_position[1]
    if x >= 9 and y >= 9:
        return False
    return True

def play(player):
    input("\nPress Enter to roll the dice!")
    roll_result = randint(1, 6)
    print("\nYou rolled a", roll_result)

    player.set_position(roll_result)
    player_position = player.get_position()

    if player_position in portals:
        player.set_position(0, portals[randint(0, len(portals) - 1)])
        player_position = player.get_position()
        print("\nYou were teleported by a portal!")

    print(player_position)


# I N I T I A L I S A T I O N
print(Color.CYAN + "PLAYER 1" + Color.END)
player1 = Player(input("Name: "), [0, 0], "CYAN")
player1_position = player1.get_position()

print(Color.RED + "PLAYER 2" + Color.END)
player2 = Player(input("Name: "), [0, 0], "RED")
player2_position = player2.get_position()

portals = []
for _ in range(15):
    p = [randint(0, 9), randint(0, 9)]
    while p in portals:
        p = [randint(0, 9), randint(0, 9)]
    portals.append(p)

board = []
for i in range(10):
    row = "[ ]" * 10
    for p in portals:
        if p[1] + i == 9:
            portal = "[O]"
            row = row[:p[0]*3] + portal + row[p[0]*3 + 3:]
    board.append(row)

print("\nHello, " + player1.get_name() + "! You are " + player1.get_avatar() + "!")
print("Hello, " + player2.get_name() + "! You are " + player2.get_avatar() + "!\n")
print("\n".join(update_board()))


# G A M E
count = 1
player = player1
while game_on(player1) and game_on(player2):
    print()
    if count & 1:
        print(Color.CYAN + "PLAYER 1'S TURN" + Color.END)
        play(player1)
    else:
        print(Color.RED + "PLAYER 2'S TURN" + Color.END)
        play(player2)
    print("\n".join(update_board()))
    count += 1


# E N D
print()
if player1_position[0] > player2_position[0]:
    print(Color.CYAN + "CONGRATULATIONS, PLAYER 1! YOU WIN!" + Color.END)
else:
    print(Color.RED + "CONGRATULATIONS, PLAYER 2! YOU WIN!" + Color.END)
print("\nT H A N K  Y O U  F O R  P L A Y I N G !")
input("\nPress Enter to quit...")
