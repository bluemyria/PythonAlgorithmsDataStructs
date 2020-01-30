from pprint import pprint


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


class Multistack:
    """
    Much better to handle w/ the size of the stacks
    if you manage the "top" you have a problem with defining
    the top(pointer) when the stacks are empty!!
    eg what does top = 0 mean? None or member 0?   
    """
    def __init__(self, stacksize, numstacks):
        self.numstacks = numstacks
        self.stacksize = stacksize
        self.array = [ 0 ] *  stacksize * self.numstacks
        #self.tops = [ x*self.stacksize for x in range(0,self.numstacks)]
        self.sizes = [ 0 ] * self.numstacks
        pprint(self.numstacks)
        pprint(self.stacksize)
        pprint(self.array)
        pprint(self.sizes)
        

    def Push(self, item, numstack):
        if numstack <= self.numstacks and not self.IsFull(numstack):
            self.array[self.stacksize*numstack + self.sizes[numstack]] = item
            self.sizes[numstack] += 1
            return True
        return False
        
    def Pop(self, numstack):
        if numstack <= self.numstacks and not self.IsEmpty(numstack):
            value = self.array[self.stacksize*numstack + self.sizes[numstack]-1]
            self.array[self.stacksize*numstack + self.sizes[numstack]-1] = 0
            self.sizes[numstack] -= 1
            return value
            
    def Peek(self, numstack):
        return self.array[self.stacksize*numstack + self.sizes[numstack]-1]

    def IsEmpty(self, numstack):
        return self.sizes[numstack] == 0

    def IsFull(self, numstack):
        return self.sizes[numstack] == self.stacksize



newstack = Multistack(5, 3)
pprint(newstack.array)

print(newstack.IsEmpty(1))
newstack.Push(3, 1)
pprint(newstack.array)
pprint(newstack.sizes)
print(newstack.Peek(1))
print(newstack.IsEmpty(1))
newstack.Push(2, 1)
newstack.Push(5, 1)
newstack.Push(7, 1)
newstack.Push(9, 1)
newstack.Push(11, 1)
pprint(newstack.array)
pprint(newstack.sizes)
print(newstack.Peek(1))
pprint(newstack.array)
pprint(newstack.sizes)
print(newstack.Pop(1))
print(newstack.Peek(1))
pprint(newstack.array)
pprint(newstack.sizes)
newstack.Push(3, 1)
pprint(newstack.array)
pprint(newstack.sizes)
newstack.Push(4, 2)
newstack.Push(2, 2)
newstack.Push(5, 2)
newstack.Push(7, 2)
newstack.Push(9, 2)
newstack.Push(11, 2)

newstack.Pop(2)

pprint(newstack.array)
pprint(newstack.sizes)