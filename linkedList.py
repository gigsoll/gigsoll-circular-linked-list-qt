class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):
        if self.last != None:
            return self.last
        newNode = Node(data)
        self.last = newNode
        self.last.next = self.last
        return self.last


    def addAtEnd(self, data):
        if self.last == None:
            return self.addToEmpty(data)
        newNode = Node(data)
        newNode.next = self.last.next
        self.last.next = newNode
        self.last = newNode
        return self.last

    def addAfter(self, data, index):
        if self.last is None:
            return self.addToEmpty(data)
        newNode = Node(data)
        current = self.last.next
        i = 0
        while i < index:
            current = current.next
            i += 1
            if current == self.last.next:
                raise IndexError("Index is out of range")
        newNode.next = current.next
        current.next = newNode
        if current == self.last:
            self.last = newNode
        return self.last
    
    def addBefore(self, data, index):
        if self.last is None:
            return self.addToEmpty(data)
        newNode = Node(data)
        if index == 0:
            newNode.next = self.last.next
            self.last.next = newNode
            return self
        current = self.last.next
        prev = None
        i = 0
        while i < index:
            prev = current
            current = current.next
            i += 1
            if current == self.last.next:
                raise IndexError("Index is out of range")
        newNode.next = current
        prev.next = newNode

    def deleteNode(self, index):
        if self.last is None:
            return IndexError("List is empty")
        if index == 0:
            if self.last.next == self.last:
                self.last = None
                return
            else:
                self.last.next = self.last.next.next
                return
        current = self.last.next
        prev = None
        counter = -1
        while current:
            counter += 1
            if counter == index:
                if current == self.last:
                    self.last = prev
                    prev.next = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            if current == self.last.next:
                return IndexError("Index out of range")

    def traverse(self):
        nodeData = []
        if self.last == None:
            return nodeData
        newNode = self.last.next
        while newNode:
            nodeData.append(newNode.data)
            newNode = newNode.next
            if newNode == self.last.next:
                return nodeData
    
    def traverseNumber(self, number):
        nodeData = []
        if self.last == None:
            return nodeData
        newNode = self.last.next
        counter = 0
        while counter < number:
            nodeData.append(newNode.data)
            newNode = newNode.next
            counter += 1
        return nodeData
    
    def search(self, index, key, way):
        if self.last == None:
            return IndexError("List is empty")
        newNode = self.last.next
        counter = -1
        while newNode:
            counter += 1
            match way:
                case "index":
                    if counter == index:
                        return newNode.data
                case "key":
                    if newNode.data == key:
                        return counter
                case "index and key":
                    if newNode.data == key and counter == index:
                        return True
            newNode = newNode.next
            if newNode == self.last.next:
                return None
