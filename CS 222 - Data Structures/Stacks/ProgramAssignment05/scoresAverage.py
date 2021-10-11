"""
Name:			        Ruben Nunez
Class and Section:	    CS 222 01
Assignment:		        Program Assignment 05
Due Date:		        Wednesday, March 31, 2021
Date Turned in:         Wednesday, March 31, 2021
Program Description:	This program allows the user to enter test scores to find 
                        the average and the letter grade of the average. It asks
                        for a score, and as long as DONE is not entered, it will
                        store them. However, if the REVERSE instruction is entered,
                        it will remove the last score stored. After the user is done
                        entering the scores, it will display the scores, the average,
                        and the letter grade for the input provided.
"""

import stack

def main():
    scores = stack.Stack()
    instruction = ""

    print("Enter the scores")
    print("Enter DONE to stop adding more scores")
    print("Enter REVERSE to change the last score added\n")

    while (instruction != "DONE"):
        try:
            instruction = input("Enter a score: ")
            if(instruction == "DONE"):
                break;
            elif (instruction == "REVERSE"):
                if(scores.isEmpty()):
                    scores.pop()
                else:
                    print("No scores have been added yet.")
            else:
                score = int(instruction)
                scores.push(score)
        except ValueError:
            print("Invalid input type, please enter a number.")

    allScores = ""
    sumOfScores = 0
    amountOfScores = scores.size()
    average = 0

    if(not scores.isEmpty()):
        while(not scores.isEmpty()):
            currentScore = scores.pop()
            print(currentScore)
            allScores += str(currentScore) + ", "
            sumOfScores += currentScore
        average = sumOfScores / amountOfScores
        allScores = allScores[0: len(allScores)-2] # Removing last ", " 
    else:
        allScores= "0 scores provided."

    letterGrade = "F"
    if(average >= 90):
        letterGrade = "A"
    elif (average >= 80):
        letterGrade = "B"
    elif (average >= 70):
        letterGrade = "C"
    elif (average >= 60):
        letterGrade = "D"

    print("\nScores:", allScores)
    print("Average:", average)
    print("Letter Grade:", letterGrade)

if __name__ == "__main__":
    main()