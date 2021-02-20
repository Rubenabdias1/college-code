team = input("Enter your team, press ENTER to quit: ")

while team != "":
    inFile = open("WorldSeriesWinners.txt", 'r')
    fileTeam = inFile.readline()
    fileTeam = fileTeam.strip()
    count = 0
    while fileTeam != "":
        if team == fileTeam:
            count += 1
        fileTeam = inFile.readline()
        fileTeam = fileTeam.strip()
    print(team, "won", count, "World Series")
    inFile.close()
    team = input("Enter your team, press ENTER to quit: ")
        
    
