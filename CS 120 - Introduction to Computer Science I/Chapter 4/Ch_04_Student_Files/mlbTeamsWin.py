teamFile = open("mlbteams.txt", 'r')

for team in teamFile:
    winnerFile = open("WorldSeriesWinners.txt", 'r')
    winner = winnerFile.readline()
    count = 0
    while winner != "":
        if winner == team:
            count += 1
        winner = winnerFile.readline()
    print(team.strip(), "won", count, "World Series")
    winnerFile.close()
