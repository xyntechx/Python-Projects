"""
A one-try, unvalidated Scrabble game
"""

from random import randint

letters = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]  # list of uppercase letters (A-Z)
inventory = []

for i in range(7):  # pick 7 letters
    letter = letters[randint(0, len(letters) - 1)]  # pick a random letter from letters
    inventory.append(letter)  # add letter to inventory

print("Possible letters to use:", inventory)

word = input("Enter word: ")

if word:  # if the user creates a word
    for char in word:
        if char not in inventory:  # if the user enters an invalid letter
            print("Please only use the letters in your inventory")
            break
        else:
            inventory.remove(char)  # ensure the user only uses each occurrence of a letter once
    else:  # if all letters are valid
        print("Awesome word!")
else:
    print("Remember to make a word!")
