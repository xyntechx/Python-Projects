def score_word(word, double_word, double_word_count, triple_word, triple_word_count, double_letters, triple_letters):
    score = 0
    word = word + double_letters + (triple_letters * 2)
    for char in word:
        score += letters_points[char]
    if double_word:
        score *= 2 ** double_word_count
    if triple_word:
        score *= 3 ** triple_word_count
    return score

letters = [chr(i) for i in range(97, 123)]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters_points = {letters: points for letters, points in zip(letters, points)}
letters_points.update({" " : 0})

# Instructions
print("Note:")
print("Types of premium squares: DW (double word), TW (triple word), DL (double letter), TL (triple letter)")
print("^^ Use the abbreviated versions when the prompt 'Enter premium square(s) used:' appears, if applicable. If multiple premium squares are used, enter the premium square names with spaces between each of them.")
print("If a DW or TW premium square is used by a word more than once, type in 'DW' or 'TW' the same number of times it is used by the word.")
print("If the same letter is on more than one DL or TL premium square, type in the letter the same number of times it uses the premium square when the prompt 'Enter letter(s):' appears.")

game_on = True
while game_on:
    has_dw, has_tw, number_of_dw, number_of_tw, double_letters, triple_letters = False, False, 0, 0, "", ""

    word = input("Enter word: ").lower()
    premium_squares = input("Enter premium square(s) used: ").upper().strip().split()
    number_of_dw, number_of_tw = premium_squares.count("DW"), premium_squares.count("TW")
    
    for premium_square in premium_squares:
        if premium_square == "DW":
            has_dw = True
        elif premium_square == "TW":
            has_tw = True
        elif premium_square == "DL":
            double_letters = input("Enter letter(s) (DL): ").lower()
        elif premium_square == "TL":
            triple_letters = input("Enter letter(s) (TL): ").lower()
    
    print(score_word(word, has_dw, number_of_dw, has_tw, number_of_tw, double_letters, triple_letters))

    end_game = input("End game? [Yes/No] ").lower()
    if end_game == "yes":
        game_on = False