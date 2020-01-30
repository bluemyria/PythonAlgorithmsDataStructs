import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    bleft = ["(", "{", "[" ]
    bright = [")", "}", "]" ]

    bstack = Stack()
    print(s)
    for ch in s:
        print(ch)
        if ch in bleft:
            print("left")
            bstack.push(bleft.index(ch))
        elif ch in bright:
            print("right")
            if bstack.isEmpty():
                return "NO"
            else:
                pop_index = bstack.pop()
                if bright.index(ch) != pop_index:
                    return "NO"
    if bstack.isEmpty():
        return "YES"
    else:
        return "NO"

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


if __name__ == '__main__':
    mystrings = ["}][}}(}][))]", "[](){()}", "()", "({}([][]))[]()", "{)[](}]}]}))}(())(", "([[)"]
    
    for s in mystrings:
        print(s)
        print("result: ", isBalanced(s))