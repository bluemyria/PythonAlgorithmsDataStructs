class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return self.items.__str__()    
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def conv2bin(num):
    s = Stack()

    while num > 0:
        s.push( num%2 )
        num = num // 2
    
    mystr = ""
    while not s.isEmpty():
        mystr = mystr + str(s.pop())  
    return mystr

print(" 4: ",conv2bin(4))
print("17: ",conv2bin(17))
print("45: ",conv2bin(45))
print("96: ",conv2bin(96)) 
    