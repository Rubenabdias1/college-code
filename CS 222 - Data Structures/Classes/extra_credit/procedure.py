class Procedure:
    def __init__(self, name, date, practicionerName, charge):
        self.name = name
        self.date = date
        self.practicionerName = practicionerName
        self.charge = charge
        
    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName

    def getDate(self):
        return self.date
    def setDate(self, newDate):
        self.date = newDate

    def getPracticionerName(self):
        return self.practicionerName
    def setPracticionerName(self, newPracticionerName):
        self.practicionerName = newPracticionerName

    def getCharge(self):
        return self.charge
    def setCharge(self, newCharge):
        self.charge = newCharge

    def __str__(self):
        formattedDate = self.date.strftime("%b %d, %Y")
        return "Procedure name: " + self.name + \
        "\n" + "Date: " + formattedDate +  \
        "\n" + "Practitioner: " + self.practicionerName + \
        "\n" + "Charge: " + str(self.charge)