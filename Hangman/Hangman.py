from random import randint

with open("words.txt") as file:
    words = [word.strip() for word in file]

def replaceBlanks(answer, blanks, word):
    blanks_list = list(blanks)
    letter_count = word.count(answer)
    while letter_count > 0:
        blanks_list[word.index(answer)*2] = answer
        word = word.replace(answer, " ", 1)
        letter_count = letter_count - 1
    return "".join(blanks_list)

word = words[randint(0, len(words)-1)].lower()
blanks = ""
for char in word:
    blanks += "_ "
blanks = blanks.strip()
tries = 0
used_letters = []

while "_" in blanks:
    print(blanks)
    print("The following letters have been used:", used_letters)
    answer = input("Enter Letter: ").lower()
    if answer in word:
        blanks = replaceBlanks(answer, blanks, word)
    else:
        print("Oops! The letter", answer, "is not in the word...")
    tries += 1
    used_letters += [answer]

print("The word is:", word)
print("Congratulations! You figured out the word in", tries, "tries!")
