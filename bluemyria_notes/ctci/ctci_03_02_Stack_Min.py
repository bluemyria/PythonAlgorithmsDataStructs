from pprint import pprint


class Stack:
    def __init__(self):
        self.items = []
        self.mins = []
    
    def __str__(self):
        return self.items.__str__()    
    
    def min(self):
        if len(self.mins) > 0:
            return self.mins[-1]
        return False

    def push(self, item):
        print("push", item)
        if len(self.mins) == 0 or \
           len(self.mins) > 0 and self.mins[-1] > item:
            self.mins.append(item)
        self.items.append(item)
        print("push", self.items, self.mins)

    def pop(self):
        if len(self.items) > 0:
            if self.peek() == self.mins[-1]:
                self.mins.pop()
            return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


newstack = Stack()
newstack.push(5)
newstack.push(6)
newstack.push(2)
newstack.push(7)
newstack.push(14)
newstack.push(3)
print(newstack)
print(newstack.min())
newstack.push(1)
newstack.push(4)
newstack.push(44)
newstack.push(2)
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
print("ok")
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
newstack.pop()
print(newstack)
print(newstack.min())
