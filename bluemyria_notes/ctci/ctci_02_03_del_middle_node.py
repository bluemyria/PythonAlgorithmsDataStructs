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
        return current

    def list_print(self):
        current = self.head
        while current:
            print(current.getData())
            current = current.getNext()        



def del_middle_node(n):
    """ SOS The last one cannot be deleted w/ this method...
    """
    if n and n.getNext():
        my_next = n.getNext()
        n.setNext(my_next.getNext())
        n.setData(my_next.getData())


mylist = SLinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)


mylist.list_print()
node = mylist.search(31)

del_middle_node(node)
print("___AFTER DEL___")
mylist.list_print()

