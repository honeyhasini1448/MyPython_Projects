questions = ("How many bones are in a human body? ",
             "Which animal lays the largest egg? ",
             "Which planet in the solar system is hottest? ",
             "How many elements are in a Periodic table? ",
             "what is the most abundant gas in earth's atmosphere? ")

options = (("A.207" ,"B.206" ,"C.205" ,"D.208" ),
           ("A.Whale" ,"B.Donkey" ,"C.Ostrich ","D.Elephant" ),
           ("A.Earth" ,"B.Jupiter" ,"C.Mercury" ,"D.Venus" ),
           ("A.118 ","B.119" ,"C.116" ,"D.117" ),
           ("A.Hydrogen" ,"B.Nitrogen" ,"C.Oxygen" ,"D.Carbondioxide" ))

answers = ("B","C","D","A","B")
guesses = []
score = 0
question_num = 0

for question in questions :
        print("-----------------------------------------------------------")
        print(question)
        for option in options[question_num] :
              print(option)


        guess = input("Enter ANS (A,B,C,D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num] :
            score += 1
            print("Correct")
        else :
            print("Incorrect")
            print(f"The correct ans is: {answers[question_num]}")

        question_num += 1

print("-----------------------------------------------------------")
print("                          RESULT                           ")
print("-----------------------------------------------------------")

print("Answers: ", end=" ")
for answer in answers :
     print(answer, end=" ")
print()

print("Guesses: ", end=" ")
for guess in guesses:
     print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is : {score}%")