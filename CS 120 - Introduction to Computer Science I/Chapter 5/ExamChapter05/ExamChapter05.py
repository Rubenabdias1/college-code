"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Performance Exam Chapter 05
Program Description:    This program asks the user for a number, then searches
                        through a list and prints the numbers that are greater
                        than the inputted number.
"""

numberList = [5, 12, 27, 35, 48, 56, 69, 71, 83, 92, 100, 109, 205, 500, 1000]
numberInput = int(input("Enter a number: "))
greaterNumbers = []
count = 0

for number in numberList:
    if number > numberInput:
        greaterNumbers.append(number)
        count += 1

if count == 0:
    print("\n", numberInput, "is greater than the numbers in the list.")
else:
    print("\nNumbers that are greater than", numberInput)
    for number in greaterNumbers:
        print(number)
