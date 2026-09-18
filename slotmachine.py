# ________________________Slot machine in Python________________________
import random

def spin_row() :
    symbols = ['🎶','🍒','🌸','🍉','⭐']
    # results = []
    # for symbol in range(3):
    #    results.append(random.choice(symbols))
    # return results
    #  ----- this above code is written in simple way using list comprehensions ----

    return [random.choice(symbols) for symbol in range(3)]

def print_row(row) :
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet) :
    if row[0] == row[1] == row[2] :
        if row[0] == '🍒' :
            return bet*2
        if row[0] == '🎶' :
            return bet*3
        if row[0] == '🌸' : 
            return bet*5
        if row[0] == '🍉' : 
            return bet*10
        if row[0] == '⭐' :
            return bet*20
    return 0

def main () :
    balance = 100 

    print("-----------------------------------------------------------")
    print("_____________Welcome to Python Slot Machine________________")
    print("________Symbols________ : 🎶 🍒 🌸 🍉 ⭐ ________________")
    print("-----------------------------------------------------------")

    while balance > 0 : 
        print(f"Current Balance: {balance}")
        bet = (input("Enter bet amount: "))

        if not bet.isdigit() : 
            print("Please enter a valid input.")
            continue
        
        bet = int(bet)

        if bet > balance :
            print("Insufficient balance funds")
            continue

        if bet <= 0 : 
            print("bet amount must be greater than zero (0).")
            continue
        

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        
        if payout > 0 : 
            print(f"You Won ${payout}")
        else :
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again(y/n): ").lower()

        if play_again == 'y':
            pass
        elif play_again == 'n':
            print("______Hope you like the slot_machine in python______\n")
            break
        else :
            print("Invalid Input !")

    print("****************************************************")
    print(f"..._GAME_OVER__... Your Final Balance is {balance}")
    print("****************************************************")

if __name__ == '__main__' : 
    main()