from node import Node

class LLQue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def enqueue(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def dequeue(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            item = current.getData()
            self.head = current.getNext()
        else:
            item = current.getData()
            previous.setNext(current.getNext())
        return item

    def __str__(self):
        msg = ""
        current = self.head
        while current != None:
            msg += str(current.getData()) + " "
            current = current.getNext()
        return msg
