class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def __str__(self):
        return str(self.data)


class UnorderedList:

    def __init__(self):
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        if self.head == None:
            self.last = temp
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def __str__(self):
        current = self.head
        s = ""
        
        while current != None:
            s = s + str(current.getData()) +", "
            current = current.getNext()
        s = s + "head: " + str(self.head) + " last: " + str(self.last)
        return s

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                if current.getNext() == None:
                    self.last = previous
                    print("previous",previous)
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            if current != None:
                previous.setNext(current.getNext())
            
    def append(self,item):       
        temp = Node(item)
        last = self.last
        print(last)
        last.setNext(temp)
        self.last = temp
        

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(31)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.append(104))
print(mylist)