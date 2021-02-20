""" 
    Name:			        Ruben Nunez
    Class and Section:	    CS 222 01
    Assignment:		        Program Assignment 01
    Due Date:		        February 5, 2021
    Date Turned in:         February 2, 2021
    Program Description:	This program stores two collections of names, one for boys
                            and the other for girls. It displays a menu for the user to
                            add and remove a name and count from the a collection, as well
                            as finding the count for a particular name, or the highest count
                            stored in the collections.
"""

def createDictionaryFromFile (path="Boys.txt"):
    f = open(path, 'r')
    dictionary = dict()

    line =  f.readline();     
    while line != "":
        # remove trailing newline characters and split in comma
        lineData = line.strip().split(',')
        # index 0 is the name and index 1 is the count
        dictionary[lineData[0]] = int(lineData[1]) #TODO: check input for type errors
        
        line =  f.readline();

    return dictionary


def askForCollectionName():
    print('\nWich collection would you like to use?')
    collection = input('Input either boys or girls. Enter 0 to go back: ')

    while collection != 'boys' and collection != 'girls' and collection != '0':
        print('Invalid collection')
        collection = input('Input either boys or girls. Enter 0 to go back: ')

    return collection


def addNameAndCount (dictionary):
    name = input('Enter the name: ')
    while name in dictionary:
        print("The name: " + name + " is already in the collection.")
        name = input('Enter the name: ')

    count = input('Enter the count: ')

    while not count.isdigit():
        print("Invalid count")
        count = input('Enter the count: ')


    dictionary[name] = int(count)

    return {"name": name, "count": int(count)}

def removeNameAndCount (dictionary):
    name = input('\nEnter the name: ')
    while name not in dictionary:
        print("The name: " + name + " is not in the collection.")
        name = input('\nEnter the name: ')

    deletedItem = {"name": name, "count": dictionary[name],}
    del dictionary[name]

    return deletedItem
    
def findCount (dictionary, name):
    if (name in dictionary):
        return dictionary[name]
    else: 
        return 0

def findHighestCount(dictionary):
    highestCount = {"name": "", "count": 0}
    for name in dictionary:
        thisCount = dictionary[name]
        if(thisCount > highestCount["count"]):
            highestCount["name"] = name
            highestCount["count"] = thisCount

    return highestCount


def main (): 
    print('Loading...')

    boysDictionary = createDictionaryFromFile("Boys.txt")
    girlsDictionary = createDictionaryFromFile("Girls.txt")

    code = "";

    while code != 0:

        print("\n=================- NAMES AND COUNTS -=================")
        print(" - Enter 1 to add a new name and count")
        print(" - Enter 2 to delete a name and count")
        print(" - Enter 3 to find the count of a name")
        print(" - Enter 4 to find the boy name with the highest count")
        print(" - Enter 5 to find the boy name with the highest count")
        print(" - Enter 0 to quit the program")

        code = input("Instruction: ")
        
        if(code.isdigit() and int(code) not in range(6)):
            print()
            print('=> !! Invalid intruction !!')
        
        code = int(code);
        
        if (code == 0):
            break;
        elif (code == 1):
            collection = askForCollectionName()
            addedItem = False

            if(collection == 'boys'):
                # Since dictionaries are mutable, there is no nee
                addedItem = addNameAndCount(boysDictionary)

            elif(collection == 'girls'):
                addedItem = addNameAndCount(girlsDictionary)

            if(addedItem):
                print("========================")
                print(addedItem["name"] + " has been named " + str(addedItem["count"]) + " times")
                
        elif (code == 2):
            collection = askForCollectionName()

            deletedItem = False

            if(collection == 'boys'):
                deletedItem = removeNameAndCount(boysDictionary)

            elif(collection == 'girls'):
                 deletedItem = removeNameAndCount(girlsDictionary)

            if(deletedItem):
                print("The name " + deletedItem["name"] + " has been deleted from the collection")

        elif (code == 3):
            name = input("Enter a name: ")
            countInBoys = findCount(boysDictionary, name)
            countInGirls = findCount(girlsDictionary, name)
            
            print("The name: " + name + ", has a count of " + str(countInBoys) + " in the boys collection, and a count of " + str(countInGirls) + " in the girls collection." )

        elif (code == 4):
            highest = findHighestCount(boysDictionary)
            print("\n" + highest['name'] + " has the highest with the count of " + str(highest['count']))
        
        elif (code == 5):
            highest = findHighestCount(girlsDictionary)
            print("\n" + highest['name'] + " has the highest with the count of " + str(highest['count']))
        

if __name__ == "__main__":
    main()