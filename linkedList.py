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
        if self.last == None:
            self.addToEmpty(data)
        newNode = Node(data)
        p = self.last.next
        counter = -1
        while p:
            counter += 1
            if counter == index:
                newNode.next = p.next
                p.next = newNode
                if p == self.last:
                    self.last = newNode
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                return IndexError("Index is not found")

    def deleteNode(self, last, key):
        if last == None:
            return
        if (last).data == key and (last).next == last:
            last = None   
        temp = last
        d = None
        if (last).data == key:
            while temp.next != last:
                temp = temp.next
            temp.next = (last).next
            last = temp.next
        while temp.next != last and temp.next.data != key:
            temp = temp.next
        if temp.next.data == key:
            d = temp.next
            temp.next = d.next
        return last

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