"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Performance Exam Chapter 04
Program Description:    This program reads the number of steps a person has
                        taken each day for a year. Then, displays the average
                        number of steps taken.
"""

stepsFile = open("steps.txt", 'r')

average = 0
step = stepsFile.readline()
numberOfDays = 0
while step != "":
    average += int(step.strip())
    numberOfDays += 1
    step = stepsFile.readline()

average /= numberOfDays #In case there are not 365

print("The average number of steps taken for a year is", int(average), "steps.")
                                                 #Steps is a integer quantity
