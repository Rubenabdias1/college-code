inFile = open("TextFileChapter5.txt", 'r')
outFile = open("copy.txt", 'w')

ch = inFile.read(1)
while ch != "":
    outFile.write(ch)
    print(ch, end="")
    ch = inFile.read(1)

inFile.close()
outFile.close()
