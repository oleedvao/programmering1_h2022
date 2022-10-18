import random
import sys

# TODO: Read from file?
words = ["World", "Pineapple", "Cat", "Python", "Armadillo"]

word_to_guess = words[random.randrange(0, len(words))]

word_to_guess_list = list(word_to_guess)

hint = ["_"] * len(word_to_guess)

hangman = '-------\n|     |\n|     {}\n|    {}{}{}\n|     {}{}\n|\n|_______\n'
body_parts = ["0", "/", "|",  "\\",  "/", "\\"]
current_body_parts = ["", "", "",  "",  "", ""]

# Removed this line, have it at the top of the loop
# print(f"Hint: {''.join(hint).capitalize()}")

lives = 6
max_lives = 6

while "_" in hint and lives > 0:
    # Print the hangman
    print(hangman.format(*current_body_parts))
    print(f"Hint: {''.join(hint).capitalize()}")
    print(f"Current lives: {lives}")
    # TODO: Print guessed characters

    print()

    # TODO: Limit guesses to unguessed characters
    guess = input("Guess a letter: ")

    # Limit input to letters
    if not guess.isalpha():
        print("\nYou cannot guess anything other than letters\n")
        continue

    # Guess whole "word" (several letters)
    for character in guess:
        if character.lower() in word_to_guess.lower():
            for index in range(len(word_to_guess_list)):
                if character.lower() == word_to_guess_list[index].lower():
                    hint[index] = character
        else:
            index = max_lives - lives
            # Move the body part from full body, to hanged body
            current_body_parts[index] = body_parts[index]
            lives -= 1

    print()

    # Add win/loose condition
    if "_" not in hint:
        print(f"Congrats! You won with {lives} lives left")
        print(f'You guessed the word: "{word_to_guess}" correctly')
    elif lives == 0:
        print(hangman.format(*current_body_parts))
        print(f"You lost! You have {lives} lives left.")
        print(f"You got: {''.join(hint).capitalize()}")
        print(f"The word was: {word_to_guess}")

    # TODO: Play again?
