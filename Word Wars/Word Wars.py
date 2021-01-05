from random import randint

def calculate_score(word):
    score = 0 # score = the length of the word multiplied by the sum of the values of each of the word's letters
    for char in word:
        score += letters_to_values[char]
    score *= len(word)
    return score

def get_word(letter, answer, difficulty):
    if difficulty == "easy":
        chances = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1] # the opponent has a 70% chance of producing a worse word and a 30% chance of producing a better word
    elif difficulty == "medium":
        chances = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] # the opponent has a 50% chance of producing a worse word and a 50% chance of producing a better word
    elif difficulty == "hard":
        chances = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1] # the opponent has a 30% chance of producing a worse word and a 70% chance of producing a better word

    index = randint(0, 9)
    level = chances[index]

    valid_words = [word for word in words if word[0] == letter and word != answer]

    higher = []
    lower = []

    for word in valid_words:
        if calculate_score(word) > calculate_score(answer):
            higher.append(word)
        else:
            lower.append(word)
    
    if level: # the opponent's word should yield a higher score
        if higher:
            opponent = higher[randint(0, len(higher) - 1)]
        else: # if no valid word is better
            opponent = lower[randint(0, len(lower) - 1)]
    else: # the opponent's word should yield a lower score
        if lower:
            opponent = lower[randint(0, len(lower) - 1)]
        else: # if no valid word is worse
            opponent = higher[randint(0, len(higher) - 1)]
    
    return opponent

with open('words.txt') as file:
    words = [word.strip() for word in file]

letters = [chr(i) for i in range(97, 123)]
values = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10] # letter values based on Scrabble
letters_to_values = {letters: values for letters, values in zip(letters, values)}

print("Welcome to Word Wars!")

difficulty = input("Select the difficulty [Easy/Medium/Hard]: ").lower()

while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Select the difficulty [Easy/Medium/Hard]: ")

turns = int(input("How many rounds do you want to play for? "))
rounds = turns

rounds_won = 0

print()

while turns:
    letter = letters[randint(0, 25)]
    print("Enter a word which starts with the letter", letter)

    answer = input("Enter Word: ")
    while answer[0] != letter:
        print("Sorry! Your word does not start with the letter", letter)
        answer = input("Enter Word: ")
    while answer not in words:
        print("Sorry! Your word is not a valid English word!")
        answer = input("Enter Word: ")

    score = calculate_score(answer)
    opponent = get_word(letter, answer, difficulty)
    opp_score = calculate_score(opponent)

    print("Your word (", answer, ") scored", score, "points!")
    print("The opponent's word (", opponent, ") scored", opp_score, "points!")
    print()

    if score > opp_score:
        rounds_won += 1

    turns -= 1

print("You won", rounds_won, "out of", rounds, "rounds!")