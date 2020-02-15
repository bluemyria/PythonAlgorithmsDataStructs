class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def __str__(self):
        return str(self.value)

class MyLinkedList:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: LinkedListNode = None
        self.length = 0
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
    
    def __str__(self):
        return " -> ".join([str(x) for x in self]) + " Head: "+ str(self.head)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr, i = self.head, 0
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr:
            return curr.value
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head: 
            self.head = LinkedListNode(val, None)
        else:
            self.head = LinkedListNode(val, self.head)
        #print(self)
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head: 
            self.head = LinkedListNode(val, None)
        else:
            curr, i = self.head, 0
            while curr and curr.next:
                curr = curr.next
            curr.next = LinkedListNode(val, None)
        #print(self)
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            return self.addAtHead(val)
        curr, i = self.head, 0
        while curr and i < index-1:
            curr = curr.next
            i += 1
        if curr:
            newNode = LinkedListNode(val, curr.next)
            curr.next = newNode
        #print(self)
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr, i = self.head, 0
        if index == 0:
            self.head = self.head.next
        else:
            while curr and i < index-1:
                curr = curr.next
                i += 1
            if curr and curr.next:
                curr.next = curr.next.next  

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.get(1)
obj.deleteAtIndex(0)
obj.get(0)
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return False
        s, f = head, head.next
        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f:
                return True
        return False


# Design Linked List
class LinkedListNode2:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def __str__(self):
        return str(self.value)

class MyLinkedList2:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: LinkedListNode = None
        self.length = 0
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
    
    def __str__(self):
        return " -> ".join([str(x) for x in self]) + " Head: "+ str(self.head)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr, i = self.head, 0
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr:
            return curr.value
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head: 
            self.head = LinkedListNode(val, None)
        else:
            self.head = LinkedListNode(val, self.head)
        #print(self)
        
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head: 
            self.head = LinkedListNode(val, None)
        else:
            curr, i = self.head, 0
            while curr and curr.next:
                curr = curr.next
            curr.next = LinkedListNode(val, None)
        #print(self)
        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            return self.addAtHead(val)
        curr, i = self.head, 0
        while curr and i < index-1:
            curr = curr.next
            i += 1
        if curr:
            newNode = LinkedListNode(val, curr.next)
            curr.next = newNode
        #print(self)
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr, i = self.head, 0
        if index == 0:
            self.head = self.head.next
        else:
            while curr and i < index-1:
                curr = curr.next
                i += 1
            if curr and curr.next:
                curr.next = curr.next.next
        #print(self)  

# Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def length(head):
            curr, length = head, 0
            while curr:
                length += 1
                curr = curr.next
            print("length", length)
            return length
        
        def advance(head, k):
            curr, progress = head, 0
            while curr and progress < k:
                progress += 1
                curr = curr.next
            print(curr.val)
            return curr
        
        lengthA = length(headA)
        lengthB = length(headB)
        
        if lengthA == 0 or lengthB == 0:
            return None        
        
        if lengthA < lengthB:
            startA, startB = headA, advance(headB, lengthB -lengthA)
        else:
            startA, startB = advance(headA, lengthA -lengthB), headB
            
        while startA and startB and startA != startB:
            startA = startA.next
            startB = startB.next
        
        return startA
