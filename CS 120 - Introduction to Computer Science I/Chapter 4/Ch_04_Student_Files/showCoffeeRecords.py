fileName = input("Enter the file name: ")
fileNameOF = False
while not FileNameOK:
    try:
        coffeeFile = open(fileName, 'r')
        fileNameOK = True
    except IOError:
        print("Wrong file name", fileName)
        fileName = input("Enter the file name: ")
line = coffeeFile.readline()
while line != "":
    data = line.split(", ")
    descr = data[0]
    qty = float(data[1])

    print("Description:", descr)
    print("Quantity: " + str(qty) + "\n")

    line = coffeeFile.readline()
coffeeFile.close()
