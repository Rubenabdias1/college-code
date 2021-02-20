file = open("dictionary.txt", 'r')
outFile = open("newDict.txt", 'w')

word = file.readline()
current = ''
count = 0
while word != "":
    try:
        if len(word) == 3 or len(word) == 4 or len(word) == 7:
            outFile.write(word)
            count += 1
        current = word
        word = file.readline()
    except:
        print(word)
        continue
print("Number of words in new file:", count)


file.close()
outFile.close()
