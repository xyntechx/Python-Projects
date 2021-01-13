import random
import colorama

colorama.init()

class Color:
    PURPLE = '\033[95m' #when using items
    GREEN = '\033[92m' #when healed
    YELLOW = '\033[93m' #when obtaining items
    RED = '\033[91m' #when damaged
    BOLD = '\033[1m' #THE VOICE
    CYAN = '\033[96m' #The Game
    END = '\033[0m'

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = {"apple": 3, "club": 1}
        self.health = 100
        self.location = [0, 0]
        self.weapons = {"sword": 10, "axe": 8, "scythe": 10, "dagger": 5, "club": 3}
        self.food = {"apple": 5, "banana": 8, "cake": 10, "chocolate": 3, "cookie": 4, "noodles": 10, "bread": 5, "carrot": 5}

    def __str__(self):
        return Color.BOLD + "You are " + self.name + " and you have 100 health points (maximum). You have these things with you: " + str(self.inventory) + Color.END
    
    def get_name(self):
        return self.name
    
    def get_inventory(self):
        return Color.BOLD + "You have these things with you: " + str(self.inventory) + Color.END

    def get_health(self):
        return Color.BOLD + "You have " + str(self.health) + " health points." + Color.END
    
    def get_health_value(self):
        return self.health

    def lose_health(self, damage):
        self.health -= damage
        if self.health > 0:
            return Color.RED + "You lost " + str(damage) + " health points. You now have " + str(self.health) + " health points left." + Color.END
        else:
            return Color.RED + "You lost " + str(damage) + " health points. You died." + Color.END

    def encounter_enemy(self, enemy):
        return Color.RED + "You have encountered a " + enemy + "!" + Color.END

    def get_location(self):
        return self.location

    def set_location(self, move):
        if move == "UP":
            if self.location[1] < 9:
                self.location[1] += 1
            else:
                print(Color.BOLD + "Oops! You seem to have hit a wall." + Color.END)
        elif move == "DOWN":
            if self.location[1] > 0:
                self.location[1] -= 1
            else:
                print(Color.BOLD + "Oops! You seem to have hit a wall." + Color.END)
        elif move == "LEFT":
            if self.location[0] > 0:
                self.location[0] -= 1
            else:
                print(Color.BOLD + "Oops! You seem to have hit a wall." + Color.END)
        elif move == "RIGHT":
            if self.location[0] < 9:
                self.location[0] += 1
            else:
                print(Color.BOLD + "Oops! You seem to have hit a wall." + Color.END)

    def obtain_item(self, item):
        if item not in self.inventory:
            self.inventory[item] = 1
        else:
            self.inventory[item] += 1
        return Color.YELLOW + "You obtained a(n)/some " + item + "." + " You now have these things with you: " + str(self.inventory) + Color.END

    def use_item(self, item):
        if item in self.inventory.keys() and self.inventory[item] > 0 and item in self.food:
            if self.health < 100:
                self.health += self.food[item]
                if self.health > 100:
                    self.health -= self.health - 100
                self.inventory[item] -= 1
                usage = Color.PURPLE + "You ate a(n)/some " + item + "." + " You now have " + str(self.inventory[item]) + " " + item + "(s) left." + Color.END
                health_up = Color.GREEN + "You now have " + str(self.health) + " health points." + Color.END
                return usage + '\n' + health_up
            else:
                return Color.BOLD + "You still have maximum health points." + Color.END
        elif item in self.inventory.keys() and self.inventory[item] > 0 and item in self.weapons.keys():
            return Color.PURPLE + "You inflicted " + str(self.weapons[item]) + " damage points." + Color.END 
        elif item not in self.inventory.keys() or self.inventory[item] == 0:
            return Color.BOLD + "You don't have a(n)/some " + item + "." + Color.END

    def do_damage(self, weapon):
        if weapon in self.inventory.keys() and self.inventory[weapon] > 0 and weapon in self.weapons.keys():
            return self.weapons[weapon]

class Enemy:
    def __init__(self):
        self.name = "enemy"
        self.health = 0
        self.damage = 0
    
    def get_health(self):
        return self.health
    
    def lose_health(self, damage):
        self.health -= damage
        if self.health > 0:
            return Color.PURPLE + "The " + self.name + " lost " + str(damage) + " health points. It now has " + str(self.health) + " health points left." + Color.END
        else:
            return Color.PURPLE + "The " + self.name + " lost " + str(damage) + " health points. It died." + Color.END

    def do_damage(self):
        return self.damage

    def get_name(self):
        return self.name

class Bandit(Enemy):
    def __init__(self):
        self.name = "Bandit"
        self.health = 10
        self.damage = 5

class Sorcerer(Enemy):
    def __init__(self):
        self.name = "Sorcerer"
        self.health = 20
        self.damage = 15

class Zombie(Enemy):
    def __init__(self):
        self.name = "Zombie"
        self.health = 15
        self.damage = 10

class Bomber(Enemy):
    def __init__(self):
        self.name = "Bomber"
        self.health = 5
        self.damage = 20

def get_key(val, d):
    for key, value in d.items():
        if val == value:
            return key


# G A M E
end = [random.randint(1, 9), random.randint(1, 9)]

object_choices = ["apple", "banana", "cake", "chocolate", "cookie", "noodles", "bread", "carrot", "sword", "axe", "scythe", "dagger", "club"]
objects = {}
for i in range(25):
    o = random.choice(object_choices)
    objects[o] = [random.randint(1, 9), random.randint(1, 9)]
    while objects[o] == end or list(objects.values()).count(objects[o]) > 1:
        objects[o] = [random.randint(1, 9), random.randint(1, 9)]

enemy_choices = [Bandit(), Sorcerer(), Zombie(), Bomber()] 
enemies = {}
for i in range(10):
    e = random.choice(enemy_choices)
    enemies[e] = [random.randint(1, 9), random.randint(1, 9)]
    while enemies[e] == end or list(enemies.values()).count(enemies[e]) > 1:
        enemies[e] = [random.randint(1, 9), random.randint(1, 9)]
        
name = input("Who am I? Name: ")
player = Player(name)
print("Where am I?")
print("I can't see...")
print(player)
print("Wait... who are you?")
print(Color.BOLD + "I am The Voice." + Color.END)
print(Color.BOLD + "You have to escape this maze, " + player.get_name() + "." + Color.END)
print("Oh... okay. How should I do this? I can't see anything!")
print(Color.BOLD + "Just type 'UP', 'DOWN', 'LEFT', or 'RIGHT' to move." + Color.END)
print(Color.BOLD + "To check your inventory or health, type 'I' or 'H' respectively." + Color.END)
print(Color.BOLD + "You can eat and regain your health when you type 'EAT' followed by a space then the food of your choice, given that you have the food." + Color.END)
print(Color.BOLD + "To damage an enemy when you encounter one, type 'ATTACK' followed by a space then the weapon of your choice, given that you have the weapon." + Color.END)
print(Color.BOLD + "I will tell you what happens after you make every move." + Color.END)
print("Alright. Sounds simple enough.")
print()
print(Color.CYAN + "E S C A P E" + Color.END)
print()

game_on = True
while game_on:
    action = input("What should I do? Action: ").strip().upper()
    if action == "I":
        print(player.get_inventory())
    elif action == "H":
        print(player.get_health())
    elif "EAT" in action:
        print(player.use_item(action.split()[1].lower()))
    elif action == "UP" or action == "DOWN" or action == "LEFT" or action == "RIGHT":
        player.set_location(action)
    else:
        print(Color.BOLD + "Please enter a recognized command." + Color.END)

    if player.get_location() in objects.values():
        obj = get_key(player.get_location(), objects)
        print(player.obtain_item(obj))
        del objects[obj]

    if player.get_location() in enemies.values():
        enemy = get_key(player.get_location(), enemies)
        print(player.encounter_enemy(enemy.get_name()))
        del enemies[enemy]
        while enemy.get_health() > 0 and player.get_health_value() > 0:
            action = input("I can't move until I've defeated the enemy! What should I do? Action: ").strip().upper()
            if "ATTACK" in action:
                print(player.use_item(action.split()[1].lower()))
                print(enemy.lose_health(player.do_damage(action.split()[1].lower())))
            elif action == "I":
                print(player.get_inventory())
            elif action == "H":
                print(player.get_health())
            elif "EAT" in action:
                print(player.use_item(action.split()[1].lower()))
            else:
                print(Color.BOLD + "Please enter a recognized command." + Color.END)
            
            if enemy.get_health() <= 0:
                break
            else:
                print(player.lose_health(enemy.do_damage()))

    if player.get_location() == end:
        game_on = False
        print(Color.BOLD + "Congratulations, " + player.get_name() + ". You have escaped the maze safely!" + Color.END)
    
    if player.get_health_value() <= 0:
        game_on = False
        print(Color.BOLD + "Game Over... Goodbye, " + player.get_name() + "." + Color.END)

input(Color.CYAN + "Press 'Enter' to quit..." + Color.END)
        
