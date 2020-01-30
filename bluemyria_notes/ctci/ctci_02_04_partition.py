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



def partition(ll,num):
    """ SOS when small list remains empty!
    """
    small_list = SLinkedList()
    big_list = SLinkedList()
    
    head_added = False
                
    n = ll.getHead()
    while n:
        data = n.getData()
        if data < num:
            small_list.add(data)
            if not head_added:
                head_added = True
                small_list_last = small_list.getHead()
        else:
            big_list.add(data)
        n = n.getNext()
    print("___SMALL___")
    small_list.list_print()
    print("___BIG___")
    big_list.list_print()
    print("___ADDING___")
    if head_added:
        small_list_last.setNext(big_list.getHead())
    else:
        small_list = big_list
    small_list.list_print()
    
    return small_list
     


mylist = SLinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)


mylist.list_print()
print("___BEFORE PART___")
mypart = partition(mylist, 30)
print("___AFTER PART___")
mypart.list_print()

