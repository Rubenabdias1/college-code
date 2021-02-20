"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Program Assignment 03, Chapter 03
Program Description:    This program asks the user for the starting salary, the
                        percentage increase and the  years in schedule then
                        prints out a table with the salaries in every scheduled
                        year.
"""

startingSalary = float(input("Enter the starting salary: "))
increasePercent = int(input("Enter the percentage of increase: "))
years = int(input("Enter the number of years in the schedule: "))

actualSalary = startingSalary
increasePercent /= 100.0

print("%-5s%9s"%("Year","Salary"))
for year in range(1, years + 1):
    print("%-5d%11.2f"%(year, actualSalary))
    actualSalary *= (1 + increasePercent)

if increasePercent >= 0.1 :
    print("\nThe percentage increase is more than 10%.")

if years <= 0 :
    print("The number of years is not greater than 0.")
