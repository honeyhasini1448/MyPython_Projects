import random
options = ("rock", "paper", "scissors")
running = True 

print("_________Welcome to Python { ROCK PAPER SCISSORS } game________")
print()

while running :

    player = None 
    computer = random.choice(options)

    while player not in options :
        player = input("Enter Your choice (Rock,Paper,Scissors): ").lower()

    if player == computer :
            print("its a Tie")
    elif player == "rock" and computer == "paper":
            print("Oops Computer Won!")
    elif player == "rock" and computer == "scissors":
            print("Hurray! You Won")
    elif player == "paper" and computer == "rock":
            print("Hurray! You Won")
    elif player == "paper" and computer == "scissors":
            print("Oops Computer Won!")
    elif player == "scissors" and computer == "paper":
            print("Hurray! You Won")
    elif player == "scissors" and computer == "rock" :
            print("Oops Computer Won!")

    print(f"Computer Choice:{computer}")
    print(f"Player Choice:{player}")

    play_again = input("Want to play again (y/n): ").lower()
    if not play_again == "y" :
           running = False 

print()
print("Thanks for Playing RockPaperScissors in python")
print()