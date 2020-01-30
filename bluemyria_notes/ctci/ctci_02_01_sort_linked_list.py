class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext



class SLinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head)
        self.head = tmp

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current and not found:
            print(current.getData())
            if current.getData() == item:
                previous.setNext(current.getNext())
                found = True 
            previous = current
            current = current.getNext()
        return found

    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.getNext()
        return size
    
    def search(self, item):
        current = self.head
        found = False
        while current and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def list_print(self):
        current = self.head
        while current:
            print(current.getData())
            current = current.getNext()        

def remove_dups(ll):
    """
    REMEMBER:  current != None and current.getNext() != None
    otherwise
    AttributeError: 'NoneType' object has no attribute 'getNext'

    https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter2/1_Remove_Dups.py
    is much better (remove_dups_followup)  :(
    """
    current = ll.getHead()
    dup_found = False
    if current == None:
        return dup_found
    
    prev_runner = current
    runner = current.getNext()

    val = current.getData()

    while current != None and current.getNext() != None:
        while runner != None:
            print(current.getData(), prev_runner.getData(), runner.getData())
            if runner.getData() == val:
                prev_runner.setNext(runner.getNext())
                runner = runner.getNext() 
                dup_found = True
            else:
                prev_runner = runner
                runner = runner.getNext()
        print("after runner")
        current = current.getNext()
        prev_runner = current
        if current != None and current.getNext() != None:
            runner = current.getNext()
            val = current.getData()
    return dup_found








mylist = SLinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)


mylist.list_print()
print(mylist.search(17))
mylist.remove(17)
print(mylist.search(17))

mylist.list_print()

print("___START LLIST___")
llist = SLinkedList()
#llist.add(100)
llist.add(3)
llist.add(45)
llist.add(3)
llist.add(10)
llist.add(45)
llist.add(3)

llist.list_print()
print("___START DUB___")
remove_dups(llist)
print("___END DUB___")

llist.list_print()


print("___START LLIST___")
llist = SLinkedList()
#llist.add(100)
llist.add(3)
llist.add(3)
llist.add(3)
llist.add(3)
llist.add(3)
llist.add(3)

llist.list_print()
print("___START DUB___")
remove_dups(llist)
print("___END DUB___")

llist.list_print()
