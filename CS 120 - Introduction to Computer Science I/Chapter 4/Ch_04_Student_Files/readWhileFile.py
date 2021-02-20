inFile = open("integers.txt", 'r')
theSum = 0
for line in inFile:
    line = line.strip()
    number = int(line)
    theSum += number
print("The sum is", theSum)
inFile.close()
