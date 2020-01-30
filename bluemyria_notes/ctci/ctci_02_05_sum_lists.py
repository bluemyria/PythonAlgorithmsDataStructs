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
    """
    the linked list has been reversed!!! added items go to the back!!
    """
    def __init__(self):
        self.head = None
        self.last = self.head

    def getHead(self):
        return self.head

    def getLast(self):
        return self.last


    def isEmpty(self):
        return self.head == None

    def add(self, item):
        tmp = Node(item)
        if self.last == None:
            self.head = tmp
        else:
            self.last.next = tmp
        self.last = tmp

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
        return current

    def list_print(self):
        current = self.head
        while current:
            print(current.getData())
            current = current.getNext()        



def sum_lists(ll_a, ll_b):
    """
    the linked list has been reversed!!! added items go to the back!!
    """
    a = ll_a.getHead()
    b = ll_b.getHead()
    if  a == None:
        return ll_b 
    if  b == None:
        return ll_a

    res = SLinkedList()

    rest = 0
    
    while a or b:
        summant_a = 0 if a == None else a.getData()
        summant_b = 0 if b == None else b.getData()
        sum = summant_a + summant_b + rest 
        res.add(sum%10)
        rest = sum//10
        a = None if a == None else a.getNext()
        b = None if b == None else b.getNext()
    if rest:
        res.add(rest)
    #res.list_print()
    return res



my_a = SLinkedList()
my_a.add(9)
my_a.add(8)
my_a.add(7)

my_b = SLinkedList()
my_b.add(8)
my_b.add(6)
#my_b.add(4)

print("___A___")
my_a.list_print()
print("___B___")
my_b.list_print()

mysum = sum_lists(my_a, my_b)
print("___AFTER SUM___")
mysum.list_print()

