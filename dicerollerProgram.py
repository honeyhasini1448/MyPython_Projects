import random
print()
print("________Hello Welcome to Dice Roller Program_______")
print()

running = True

while running : 

    dice_ascii_art = {
         1 : ( "|       |",
               "|   o   |",
               "|       |" ),

         2 : ( "| o     |",
               "|       |", 
               "|     o |" ),

         3 : ( "| o     |",
               "|   o   |",
               "|     o |" ),
    
         4 : ( "| o   o |",
               "|       |",
               "| o   o |" ),

         5 : ( "| o   o |",
               "|   o   |",
               "| o   o |" ),

         6 : ( "| o   o |",
               "| o   o |",
               "| o   o |" )
    }

    no_of_dices = int(input("Enter No.of dices to roll: "))
    dice_list = []
    total = 0

    for dice in range(no_of_dices) :
        dice_list.append(random.randint(1,6))

    #--------for vertical arrangement of dice-----------
    # for dice in range(no_of_dices) :
        # for line in dice_ascii_art.get(dice_list[dice]) :
            # print(line) 

    #--------for horizontal arrangement of dice---------
    for line in range(3) : 
         for dice in dice_list :
            print(dice_ascii_art.get(dice)[line] , end="   ")
         print()
    #---------------------------------------------------

    for dice in dice_list :
        total += dice 

    print(f"Total Sum of digits : {total}")
    print()

    play = input("Do you want to continue with program( y/n): ").lower()
    if (play == "n"):
        print()
        print("Thanks, Hope you like the Program")
        print()
        running = False
        break

    elif(play == "y"):
        pass
        
    else :
        print("input is not valid")
        play = input("Do you want to continue with program( y/n):  ").lower()



    


