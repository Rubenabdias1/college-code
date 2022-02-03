import random

userName = "nunez485641"
password = "supersecret"

minNumber = 1
maxNumber = 10

def main(): 
    numberToGuess = random.randint(minNumber,maxNumber)
    incorrect = True
    while incorrect:
        guessAttempt = int(input("Enter a number between " + str(minNumber) + " and " + str(maxNumber) + ": "))
        
        if guessAttempt < minNumber:
            print("Your guess is less than", minNumber, "Try again.")
            continue
        if guessAttempt > maxNumber:
            print("Your guess is greater than", maxNumber, "Try again.")
            continue

        if guessAttempt == numberToGuess:
            print("You won!")
            incorrect = False
        else:
            print("You failed.")
            if (guessAttempt < numberToGuess):
                print(guessAttempt, "is less than the correct answer. Try again.")
            if (guessAttempt > numberToGuess):
                print(guessAttempt, "is greater than the correct answer. Try again.")


if __name__ == "__main__":
    main()