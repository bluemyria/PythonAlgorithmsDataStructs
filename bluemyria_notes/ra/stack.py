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

mystack = Stack()
mystack.push(3.14)
mystack.push("yes")
mystack.push(5)
mystack.push(True)

print(mystack)

mystack.pop()
print(mystack)


print(mystack.size())


print(mystack)
print(mystack.isEmpty())

print(mystack.peek())


s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while balanced and index < len(symbolString):
        symbol = symbolString[index]
        if symbol in "{([":
            s.push(symbol)
        elif symbol in "})]":
            if not s.isEmpty() and matches(s.peek(),symbol):
                s.pop()
            else:
                balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(opener,closer):
    openers="{(["
    closers="})]"
    return openers.index(opener) == closers.index(closer)

print(parChecker('sdf(((sd)))'))
print(parChecker('((asdasd)'))
print(parChecker('((asd)))xcvxcv))))'))

print(parChecker('{({sdf ([][])sdf sdf}())}'))
print(parChecker('[sdf{(sdf)]'))
print(parChecker('[sdf{(sdf)]))]]]}]][{[dfgfg]}]'))


import string


def toJadenCase(s):
    l = s.split()
    nl = []
    for word in l:
        if( ord(word[0]) >= ord('a')):
            word = chr(ord(word[0])-32) + word[1:]
        nl.append(word)
    return " ".join(nl)   
def mytest(s):
    return string.capwords(s)     
    
    
print("Aow can mirrors be real if our eyes aren't real")
print(toJadenCase("How can mirrors be real if our eyes aren't real"))