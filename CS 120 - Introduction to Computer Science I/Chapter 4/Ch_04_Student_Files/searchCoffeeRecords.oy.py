found = False
search = input("Enter a description to search for: ")
coffeeFile = open("coffee.txt", 'r')
line = coffeeFile.readline()
while line != "" and not found:
    data = line.split(", ")
    if data[0] = search:
        print("Description:", data[0])
        print("Quantity:", data[1])
        print()
        found = True
    line.coffeeFile.readline()
coffeeFile.close()
if not found:
    print("That item was not found in the File.")
