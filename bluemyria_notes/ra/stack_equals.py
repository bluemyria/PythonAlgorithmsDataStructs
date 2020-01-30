#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    
    hs1 = create_curr_height_array(h1)
    hs2 = create_curr_height_array(h2)
    hs3 = create_curr_height_array(h3)

    mymin = find_min_end(hs1,hs2,hs3)

    return mymin

def find_min_end(h1,h2,h3):
    len_min = min(len(h1), len(h2), len(h3))

    shorter = h1 if len(h1) == len_min else h2 if len(h2) == len_min else h3
    for i in shorter[::-1]:
        if i in h1 and i in h2 and i in h3:
            #print(i)
            return i 
    return 0

def create_curr_height_array(h):
    curr_h = 0
    st = Stack()
    hs = []    
    for el in h[::-1]:
        st.push(el)
        curr_h += el
        hs.append(curr_h)
    return hs
         

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
    
    st1 = [3, 2, 1, 1, 1]
    st2 = [4, 3, 2]
    st3 = [1]

    st1 = [3, 2, 1, 1, 1]
    st2 = [4, 3, 2]
    st3 = [1, 1, 4, 1]
    
    print(equalStacks(st1, st2, st3))
"""

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
"""