import sys
from random import randint


def choose_message(filename: str) -> str:
    print("Loading", filename, "...")
    with open(filename) as file:
        arr = [line.strip() for line in file]
        message = arr[randint(0, len(arr) - 1)]
        return message


options = sys.argv[1:]

for option in options:
    match option:
        case "help":
            print("- - -")
            print("INSTRUCTIONS")
            print("Command: python main.py <options>")
            print("<options>: simple/aid/hospitality")
            print("Example 1: python main.py simple")
            print("Example 2: python main.py simple aid")
            print("- - -")
        case "simple":
            print(choose_message("simple.txt"))
        case "aid":
            print(choose_message("aid.txt"))
        case "hospitality":
            print(choose_message("hospitality.txt"))
        case _:
            print("something else")
