#--------------------------hangman_in_Python------------------------------#

import random
from wordslist import words

hangman_art = {
                0 : ("   ",
                     "   ",
                     "   "),
                1 : (" O ",
                     "   ",
                     "   "),
                2 : (" O ",
                     " | ",
                     "   "),
                3 : (" O ",
                     "/| ",
                     "   "),
                4 : (" O ",
                     "/| ",
                     "/  "),
                5 : (" O ",
                     "/|\\",
                     "/ "),
                6 : (" O ",
                     "/|\\",
                     "/ \\"),
}

def display_man(wrong_guesses):
    print("*****")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*****")

def display_hint(hint):
    print(" ".join(hint))

def display_ans(ans):
    print(ans)

def main():
    print("-----Hangman Game-----")
    ans = random.choice(words)
    hint = ["_"] * len(ans)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! (single alphabet at a time).")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!")

        guessed_letters.add(guess)

        if guess in ans :
            for i in range(len(ans)):
                if ans[i] == guess :
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint :
            display_man(wrong_guesses)
            display_ans(ans)
            print("__YOU_WON__")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1 :
            display_man(wrong_guesses)
            display_ans(ans)
            print("__YOU_LOSE__")
            is_running = False



if __name__ == '__main__':
    main()