import unittest

class MaxStack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.max_items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)
        new_max = item 
        if len(self.max_items) and item < self.max_items[-1]:
            new_max = self.max_items[-1]
        self.max_items.append(new_max)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        self.max_items.pop()
        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
        """Get max item """
        # If the stack is empty, return None
        if not self.items:
            return None
            
        return self.max_items[-1]

    def __str__(self):
        return " ".join(map(str,self.items))


if __name__ == '__main__':
    mystack = MaxStack()
    mystack.push(4)
    mystack.push(2)
    mystack.push(5)
    mystack.push(7)
    mystack.push(3)
    print(mystack)
    a = mystack.pop()
    print(mystack.get_max())
    print(mystack)
    a = mystack.pop()
    print(mystack.get_max())
    print(mystack)
    a = mystack.pop()
    print(mystack.get_max())
    print(mystack)
    a = mystack.pop()
    print(mystack.get_max())
    
