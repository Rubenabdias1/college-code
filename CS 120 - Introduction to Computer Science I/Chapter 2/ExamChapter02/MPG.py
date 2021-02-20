"""
Name:                   Ruben Nunez
Class and Section:      CS 120 01
Assignment:             Performance Exam Chapter 02
Program Description:    This program asks the user for the number of miles
                        driven and the gallons of gas used. Then calculates the
                        miles-per-gallon (MPG) of the car. Finally, it displays
                        the calculated number.
"""

miles = float(input("Enter the number of miles driven: "))
gallons = float(input("Enter the number of gallons of gas used: "))

milespGallon = round((miles / gallons) , 2)

print("The car's miles-per-gallon is: " + str(milespGallon), "MPG")
