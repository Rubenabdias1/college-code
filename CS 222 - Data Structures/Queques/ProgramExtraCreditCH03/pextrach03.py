""" 
Name:			        Ruben Nunez
Class and Section:	    CS 222 01
Assignment:		        Program Extra Credit Chapter 3
Due Date:		        Friday, April 16, 2021
Date Turned in:         Friday, April 16, 2021
Program Description:	A grocery store checkout line simulator that enqueues customers as they arrive.
                        Customers can have from 5 up to 15 items. The rate of the checkout line is 1 item
                        per minute. And a customer gets to the checkout every 1-5 minutes. The program will
                        calculate the average wait time for every customer that was served, and it will
                        display the amount of customers left to be served. 
"""
import random
from qu import Qu
import time

class CheckoutLine:
    def __init__(self, ipm):
        self.ipm = ipm # item per minute
        self.currentCustomer = None
        self.timeRemaining = 0

    def getTimeRemaining(self):
        return self.timeRemaining

    def tick(self):
        if self.currentCustomer != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentCustomer = None

    def serveNext(self, newCustomer):
        self.currentCustomer = newCustomer
        self.timeRemaining = newCustomer.getItems() * 60 / self.ipm

    def busy(self):
        return self.currentCustomer != None


class Customer:
    def __init__(self, time):
        self.timestamp = time
        self.items = random.randrange(1,16)

    def getStamp(self):
        return self.timestamp

    def getItems(self):
        return self.items

    def waitTime(self, currentTime):
        return currentTime - self.getStamp()


def newCustomerArrived():
    num = random.randrange(1,181)
    return num == 180

def buildLog(state, timeRemaining, arrivalTime, size):
    return {
        "state": state,
        "timeRemaining": timeRemaining,
        "arrivalTime": arrivalTime, 
        "size": size,
    }

def compareLogs(oldLog, newLog):
    return (oldLog["state"] != newLog["state"]) or (oldLog["timeRemaining"] != newLog["timeRemaining"]) or \
        (oldLog["arrivalTime"] != newLog["arrivalTime"]) or (oldLog["size"] != newLog["size"])
        
def simulation(numSeconds, itemPerMinute):
    checkoutLine = CheckoutLine(itemPerMinute)
    checkoutQueue = Qu()
    waitingTimes = []
    nextCustomerWillArriveAt = random.randrange(0, 5 * 60 + 1)
    log = {
        "state": None,
        "timeRemaining": None,
        "arrivalTime": None, 
        "size": None,
    }
    for currentSecond in range(numSeconds):
        time.sleep(1)
        newLog = buildLog(("IDLE", "Working...")[checkoutLine.busy()], ((checkoutLine.getTimeRemaining() )  // 60) + 1, ((nextCustomerWillArriveAt - currentSecond + 1)  // 60) + 1, checkoutQueue.size())
        shouldPrint = compareLogs(log, newLog)
        if(shouldPrint):
            log = newLog
            print(currentSecond + 1, " s ->",  log["state"], log["timeRemaining"], "mins left, next will arrive at: ", log["arrivalTime"], "mins. ", log["size"], "customers remaining.") 

        if (nextCustomerWillArriveAt == currentSecond):
            nextCustomerWillArriveAt = currentSecond + random.randrange(1 * 60 , 5 * 60 + 1)
            newCustomer = Customer(currentSecond)
            checkoutQueue.enqueue(newCustomer)
        if(not checkoutLine.busy()) and (not checkoutQueue.isEmpty()):
            nextCustomer = checkoutQueue.dequeue()
            waitingTimes.append(nextCustomer.waitTime(currentSecond))
            checkoutLine.serveNext(nextCustomer)
        
        checkoutLine.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print("Average Wait %6.2f mins %3d customers in line." %(averageWait / 60, checkoutQueue.size())) 


def main ():
    for i in range(10):
        simulation(60 * 60 * 2, 1)

if __name__ == "__main__":
    main()