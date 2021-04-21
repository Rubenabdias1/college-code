from node import Node

class LLStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, item):
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

    def pop(self):
        if (self.head == None): return None
        
        poppedNode = self.head
        self.head = self.head.getNext()
        
        return poppedNode.getData()

    def peek(self):
        return self.head.getData()

    def __str__(self):
        msg = ""
        current = self.head
        while current != None:
            msg += str(current.getData()) + " "
            current = current.getNext()
        return msg

