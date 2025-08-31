import random
def checkErr(num):
    return num ==3

def startNew():
    print("Weolcome to guess the number you will have 3 opportunities to guess the right number")
    answer = random.randint(1,10)
    errors = 0
    return answer,errors




def check(answer, guess):
    return answer == guess

def tryA():
    retry = input("want to play again? (please enter yes or no\n)")
    while retry not in ("yes","no"):
        retry = input("Error: message not understood please enter yes or no as an answer\n")
    return retry.lower().strip() == "yes"

