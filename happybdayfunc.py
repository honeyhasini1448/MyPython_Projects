# This file is for introduction of functions in python
# function - reusable code 
day = input("Is today your Birthday(y/n): ").lower()
if day == "y":
    def HappyBirthday(name,age) : 
        print("Happy Birthday to you!")
        print(f"Happy Birthday to {name}")
        print(f"You are {age} years old")
        print("Wish you to have a long life")

    HappyBirthday(input("Enter Your Name: "),input("Enter your Age: "))

elif day == "n":
    print("Okay! Have a Great Day")
else :
    print("Invalid input")