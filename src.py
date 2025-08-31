import logic


answer,errors=logic.startNew()
while True:
    guess = int(input("please enter your guess\n"))
    errors +=1
    if(logic.check(answer,guess)):
        print(f"Congratulations you guess {guess} correctly in {errors} attempts ")
        if(logic.tryA()):
            answer,errors = logic.startNew()  
        else:
            print("Thank you for playing guess the number!")
            break


    if(logic.checkErr(errors)):
        print(f"You ran out of guesses the answer was {answer}")
        if(logic.tryA()):
            answer,errors = logic.startNew()
        else:
            print("Thank you for playing guess the number!")
            break
    print(f"You have {3-errors} attempts left")
