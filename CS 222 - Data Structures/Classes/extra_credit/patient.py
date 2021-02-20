class Patient:

    def __init__ (self,firstName, middleName, lastName, address, city, state, zipCode, phoneNumber, contactName, contactPhoneNumber):
        self.firstName = firstName
        self.middleName = middleName 
        self.lastName = lastName 
        self.address = address
        self.city = city
        self.state = state 
        self.zipCode = zipCode
        self.phoneNumber = phoneNumber
        self.contactName = contactName
        self.contactPhoneNumber = contactPhoneNumber

    def getFirstName(self):
        return self.firstName
    def setFirstName(self,newfirstName):
        self.firstName = newfirstName
        
    def getMiddleName(self):
        return self.middleName
    def setMiddleName(self, newMiddleName):
        self.middleName = newMiddleName
        
    def getLastName(self):
        return self.lastName
    def setLastName(self, newLastName):
        self.lastName = newLastName
        
    def getAddress(self):
        return self.address
    def setAddress(self, newAddress):
        self.address = newAddress
        
    def getCity(self):
        return self.city
    def setCity(self, newCity):
        self.city = newCity
        
    def getState(self):
        return self.state
    def setState(self, newState):
        self.state = newState
        
    def getZipCode(self):
        return self.zipCode
    def setZipCode(self, newZipCode):
        self.zipCode = newZipCode
        
    def getPhoneNumber(self):
        return self.phoneNumber
    def setPhoneNumber(self, newPhoneNumber):
        self.phoneNumber = newPhoneNumber
        
    def getContactName(self):
        return self.contactName
    def setContactName(self, newContactName):
        self.contactName = newContactName
        
    def getContactPhoneNumber(self):
        return self.contactPhoneNumber
    def setContactPhoneNumber(self, newContactPhoneNumber):
        self.contactPhoneNumber = newContactPhoneNumber
        
    def __str__(self):
        return "Patient: " + self.firstName + " " + self.middleName + " " + self.lastName + \
        "\n" + "Address: " + self.address + \
        "\n" + "City: " + self.city + \
        "\n" + "State: " + self.state  + \
        "\n" + "Zip Code: " + self.zipCode + \
        "\n" + "Phone Number: " + self.phoneNumber + \
        "\n" + "Contact Name: " + self.contactName + \
        "\n" + "Contact Phone Number: " + self.contactPhoneNumber