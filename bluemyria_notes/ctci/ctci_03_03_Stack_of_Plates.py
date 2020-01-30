from pprint import pprint
import unittest


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




class StackOfPlates:
    """
    Vergiss nicht die Werte zu returnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """
    def __init__(self, stacksize):
        self.stacks = []
        self.stacksize = stacksize
        self.stacknr = 0

    def __str__(self):
        print(self.stacks)
        return self.stacks.__str__()    
    
    def push(self, item):
        if self.stacknr == 0 or self.stacknr > 0 and self.stacks[-1].size() == self.stacksize:
            newstack = Stack()
            newstack.push(item)
            self.stacks.append(newstack)
            self.stacknr += 1
        else:
            self.stacks[-1].push(item)

    def pop(self):
        if self.stacknr > 0:
            value = self.stacks[-1].pop()
            if(self.stacks[-1].size()) == 0:
                del self.stacks[-1]
                self.stacknr -= 1
            return value
        else:
            return None

    def peek(self):
        if self.stacknr > 0:
            return self.stacks[-1].peek()
        else:
            return None
    
    def isEmpty(self):
        return self.stacknr == 0

    def size(self):
        return (self.stacknr-1)*self.stacksize + len(self.stacks[-1])


stacks = StackOfPlates(5)
print(stacks.stacks)
for i in range(35):
    stacks.push(i)
pprint(stacks.stacks)
lst = []
for k in range(35):
    lst.append(stacks.pop())
    pprint(stacks.stacks)
    print("lst",lst)
print(lst)
pprint(stacks.stacks)
print(list(reversed(range(35))))
