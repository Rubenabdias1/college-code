outFile = open("videos.txt", 'w')
runTime = input("Enter running time, ENTER to quit: ")
while runTime != "":
    outFile.write(runTime + "\n")
    runTime = input("Enter running time, ENTER to quit: ")
outFile.close()
print("The times have been saved to videos.txt")
modifyCoffeeRecords.py
