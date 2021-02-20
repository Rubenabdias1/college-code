""" 
Name:			        Ruben Nunez
Class and Section:	    CS 222 01
Assignment:		        Program Assignment 02
Due Date:		        Wednesday, Febraury 17, 2021
Date Turned in:         Tuesday, Febraury 16, 2021
Program Description:    This program tests all properties and
                        methods of the Pet class. It displays
                        a menu to allow the user to create
                        multiple pets, visualize them, or
                        modify a pets attributes.

"""
import pet

# You did way more than what was required.  This makes it more difficult
# for me to make sure you included all the required aspects of the
# assignment.  Please try not to make the assignment results too complicated

def createPet():
    name = input("Enter the name of your new pet: ")
    animalType = input("Enter the type of your pet: ")
    while True:
        try:
            age = int(input("Enter the age of your pet: "))
            break
        except ValueError:
            print("Invalid input for age, expected a numeric value.")

    newPet = pet.Pet(name, animalType, age)
    print("This is your new pet:")
    print(f"Name: {newPet.getName()}")
    print(f"Type: {newPet.getAnimalType()}")
    print(f"Age:  {newPet.getAge()}")
    return newPet

def displayPets(pets):
    print("Here are all your pets:")
    for pet in pets:
        print(f"- {pet}")

def selectPet(pets):
    print("Choose a pet to change its attributes:")
    for index in range(len(pets)):
        currentPet = pets[index]
        print(f"{index + 1}. {currentPet.getName()}")
    while True:
        try:
            index = int(input("\nEnter the pet's number here: ")) - 1
            selectedPet = pets[index]
            break
        except ValueError:
            print("Invalid input for pet number, expected a numeric value.")
        except IndexError:
            print(f"Pet number {index} not found.")

    return {"index": index, "pet": selectedPet}

def modifyPet(selectedPet):
    print("\nHere are the attributes:\n" + \
          "1. Name\n" + \
          "2. Type\n" + \
          "3. Age")
    prompt = input("Enter the number of the attribute you would like to change. " +
                   "Enter anything else to cancel and go back: ")
    if (prompt == "1"):
        newName = input("\nEnter the new name: ")
        selectedPet.setName(newName)
    elif (prompt == "2"):
        newAnimalType = input("\nEnter the new type: ")
        selectedPet.setAnimalType(newAnimalType)
    elif (prompt == "3"):
        while True:
            try:
                newAge = int(input("Enter the new age: "))
                break
            except ValueError:
                print("Invalid input for age, expected a numeric value.")
        selectedPet.setAge(newAge)
    
    print(f"Pet modified successfully. Now {selectedPet}")
    return selectedPet;
    
def main( ):
    print(" -- Welcome to PetApp!")

    pet1 = pet.Pet("Milo", "Dog", 2)
    pet2 = pet.Pet("Oscar", "Goldfish", 1)
    pets = [pet1, pet2]

    while True:
        print("\nMenu")
        print("1. Enter 1 to exit.")
        print("2. Enter 2 to see all your pets.")
        print("3. Enter 3 to create a new pet.")
        print("4. Enter 4 to change your pet's attributes.")
        prompt = input("What do you want to do?: ")
        print()
        if (prompt == "1"):
            break
        elif (prompt == "2"):
            displayPets(pets)
        elif (prompt == "3"):
            pets.append(createPet())
        elif (prompt == "4"):
            selectedPet = selectPet(pets)
            modifyPet(selectedPet["pet"])

if __name__ == "__main__":
    main()
