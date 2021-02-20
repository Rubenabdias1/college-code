"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Final Project Chapter 09
Due Date:               Monday, May 4, 2020
Date Turned in:         Monday, May 4, 2020
Program Description:    This program creates a Person Class. Then, creates three
                        instances of the class and tests the accessor and
                        mutator methods of the class properties. The program
                        also tests the _STR_ method of the class on a print
                        function for one of its instances.
"""

class Person():
    """Represent a person"""
    def __init__(self, name, address, age, phoneNumber):
        """Constructor that creates a Person with the given name, address, age,
        and phone number. """
        self.name = name
        self.address = address
        self.age = age
        self.phoneNumber = phoneNumber
    
    def getName(self):
        """Returns the Person's name."""
        return self.name
    def setName(self, newName):
        """Resets the person's name"""
        if type(newName) == type(""):
            self.name = newName
    
    def getAddress(self):
        """Returns the Person's address."""
        return self.address
    def setAddress(self, newAddress):
        """Resets the person's address"""
        if type(newAddress) == type(""):
            self.address = newAddress
    
    def getAge(self):
        """Returns the Person's age."""
        return self.age
    def setAge(self, newAge):
        """Resets the person's age"""
        if type(newAge) == type(""):
            self.age = newAge
    
    def getPhoneNumber(self):
        """Returns the Person's phone number."""
        return self.phoneNumber
    def setPhoneNumber(self, newPhoneNumber):
        """Resets the person's phone number"""
        if type(newPhoneNumber) == type(""):
            self.phoneNumber = newPhoneNumber
    
    def __str__(self):
        "Returns the string representation of the person"
        return "Name: " + self.name + \
            "\nAddress: " + self.address + \
                "\nAge: " + self.age + \
                    "\nPhone Number: " + self.phoneNumber


def main():
    peter = Person("Peter Pan", "8 Arcadia Lane Duarte, CA 91010", "20", \
        "308-789-1148")
    maria = Person("Maria Hills", "937 Silver Spear Court Oxnard, CA 93035", "31", \
        "805-200-9947")
    john = Person("John Snow", "18 Constitution Street Los Angeles, CA 90004", "45", \
        "213-200-9582")
    
    print("\nOld Name: " + john.getName())
    john.setName("John Flame")
    print("New Name: " + john.getName())

    print("\nAge: " + maria.getAge())
    maria.setAge("25")
    print("New Age: " + maria.getAge())

    print("\nPrevious Address: " + peter.getAddress())
    peter.setAddress("61 W. Strawberry Ave. Los Angeles, CA 90037")
    print("New Address: " + peter.getAddress())

    print("\nOld Phone Number: " + peter.getPhoneNumber())
    peter.setPhoneNumber("213-202-3306")
    print("New Phone Number: " + peter.getPhoneNumber())

    print("\n")
    print(john)

if __name__ == "__main__":
    main()
