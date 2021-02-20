# The Pet class simulates a pet.
class Pet:
    # The __init__ method initializes the
    # __name, __animalType, and __age
    # attributes with the given values
    def __init__ (self, name, animalType, age):
        self.__name = name
        self.__animalType = animalType
        self.__age = age

    # The accessor method for __name
    def getName (self):
        return self.__name;
    # The mutator method for __name
    def setName (self, name):
        self.__name = name

    # The accessor method for __animalType
    def getAnimalType (self):
        return self.__animalType
    # The mutator method for __animalType
    def setAnimalType (self, animalType):
        self.__animalType = animalType

    # The accessor method for __age
    def getAge (self):
        return self.__age
    # The mutator method for __age
    def setAge (self, age):
        self.__age = age

    # You are not allowed to use features not covered in class
    # While it may be easier to look up how to do something on Internet
    # you need to stay with what we do in class.  I have no way of knowing
    # if you actually understand what you did here or just copied it.
    def __str__(self):
        return f"{self.__name} is a {self.__animalType}" + \
               f" and is {self.__age} years of age."

