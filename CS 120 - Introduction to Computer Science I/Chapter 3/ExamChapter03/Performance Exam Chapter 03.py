"""
Name:                   Ruben Nunez
Class and Section:      CS 120 01
Assignment:             Performance Exam Chapter 03
Program Description:    This program asks the user for the bugs collected
                        every day and then displays a table with the data
                        collected. After that it asks the user if they want
                        to know the average of bugs collected. If they answer
                        yes, the program will display it.
"""
total = 0
for day in range(1, 6):
    bugsDay = int(input("Enter the number of bugs collected in day " \
                        + str(day) + ": "))
    total += bugsDay
    if day == 1:
        bugsDay1 = bugsDay
    elif day == 2:
        bugsDay2 = bugsDay
    elif day == 3:
        bugsDay3 = bugsDay
    elif day == 4:
        bugsDay4 = bugsDay
    elif day == 5:
        bugsDay5 = bugsDay
print("\n%4s%16s" % ("Days", "Bugs Collected") \
      + "\n%4s%12d" % ("1", bugsDay1) \
      + "\n%4s%12d" % ("2", bugsDay2) \
      + "\n%4s%12d" % ("3", bugsDay3) \
      + "\n%4s%12d" % ("4", bugsDay4) \
      + "\n%4s%12d" % ("5", bugsDay5))
print("The total number of bugs is:", total)
answer = input("\nWould you like to know the average number of bugs collected? ")
if answer == "yes" :
    average = (bugsDay1 + bugsDay2 + bugsDay3 + bugsDay4 + bugsDay5) / 5
    print("The average number of bugs is", "%0.2f" % average)
