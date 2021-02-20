"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Program Assignment 05
Due Date:               Friday, March 27, 2020
Date Turned in:         Friday, March 27, 2020
Program Description:    This program displays a menu where the user can choose
                        between listing the winning team of the Super Bowl of
                        an input year, count how many times a team has won the
                        Super Bowl, count how many times a team has been on one
                        or quit the program.
"""

file = open("superBowlData.txt",'r')
years = []
winningTeams = []
losingTeams = []

yearPlayed = file.readline()
while yearPlayed != "":
    playedYear = yearPlayed.split("\n")[0].split(",")
    years.append(playedYear[0])
    winningTeams.append(playedYear[1])
    losingTeams.append(playedYear[2])
    yearPlayed = file.readline()

def winnerByYear(year):
    yearIndex = years.index(year)
    winnerOfYear = winningTeams[yearIndex]
    return winnerOfYear
    
def winCount(team):
    count = 0
    if team in winningTeams:
        for winner in winningTeams:
            if winner == team:
                count += 1
    return count

def playCount(team):
    wins = winCount(team)
    count = 0
    for loser in losingTeams:
        if loser == team:
            count += 1
    loses = count
    plays = wins + loses
    return plays
    
def main():
    print("Super Bowl")
    print(" -  Enter 1 to display the winner of a particular year.")
    print(" -  Enter 2 to count how many times a particular team has won.")
    print(" -  Enter 3 to count how many times a particular team has played.")
    print(" -  Enter 4 to quit.")

    action = 0
    while action != 4:
        while action not in range(1,5):
            action = int(input("\nWhat do you want to do?: "))
            if action not in range(1,5):
                print("Invalid action")
        if action == 1:
            year = "";
            while year not in years:
                year = input("Enter the year: ")
                if year not in years:
                    print("Invalid year")
            print("The", winnerByYear(year), "won the Super Bowl in", year)
            action = 0
        elif action == 2:
            team = input("Enter the winning team: ")
            print(team, "won the Super Bowl", winCount(team), "times")
            action = 0
        elif action == 3:
            team = input("Enter a team: ")
            print("The", team, "has played", playCount(team), "Super Bowls.")
            action = 0
        else:
            print("Good Bye!")
            
if __name__ == "__main__":
    main()
