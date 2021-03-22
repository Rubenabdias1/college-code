class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice

    def getSymbol(self):
        return self.symbol
    def setSymbol(self,newSymbol):
        self.symbol = newSymbol

    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
        
    def getPreviousClosingPrice(self):
        return self.previousClosingPrice
    def setPreviousClosingPrice(self, newPreviousClosingPrice):
        self.previousClosingPrice = newPreviousClosingPrice
        
    def getCurrentPrice(self):
        return self.currentPrice
    def setCurrentPrice(self, newCurrentPrice):
        self.currentPrice = newCurrentPrice

    def getChangePercent(self):
        if(self.currentPrice == self.previousClosingPrice):
            changePercent = 0.00;
        elif(self.currentPrice > self.previousClosingPrice):
            changePercent = ((self.currentPrice - self.previousClosingPrice) / self.currentPrice)* 100
        else:
            changePercent = ((self.currentPrice - self.previousClosingPrice) / self.currentPrice)* -100
        return changePercent

    def __str__(self):
        changeSign = ""
        if self.getCurrentPrice() > self.getPreviousClosingPrice():
            changeSign = "+"
        elif self.getCurrentPrice() < self.getPreviousClosingPrice():
            changeSign = "-"

        changePercent = "Change Percent: %s%7.2f" % (changeSign,self.getChangePercent()) + "%"

        return "- %s\nSymbol: %17s\nCurrent Price: %10.4f\nPrevious Price: %9.4f\n" \
                %(self.getName(), self.getSymbol(), self.getCurrentPrice(), self.getPreviousClosingPrice() ) \
                + changePercent