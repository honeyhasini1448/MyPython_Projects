import random

low_num = 1 
high_num = 100 
guesses = 0
running = True 

answer = random.randint(low_num,high_num)
print()
print("______WELCOME to - Python Number Guessing Game______")
print(f"Select a number between {low_num} and {high_num}")
print()
while running :
    guess = input("Enter Your Guess: ")

    if guess.isdigit() :
        guess = int(guess)
        guesses += 1 
        if guess > high_num or guess < low_num :
            print("Number is out of Range")
            print(f"Please Select a number btw {low_num} and {high_num}")
        elif guess > answer :
            print("Too High, Try again")
        elif guess < answer : 
            print("Too Low,  Try again")
        elif guess == answer :
            print("You Guessed Correctly")
            print(f"No.of Guesses: {guesses}")
            running = False
    else :
        print("Invalid Guess")
        print(f"Please Select a number btw {low_num} and {high_num}")

        
    
      
