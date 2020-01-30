from LinkedList import LinkedList


def is_palindrome(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    
    if fast:
        slow = slow.next
    
    while slow and slow.next:
        if slow.value != stack.pop():
            return False
        else:
            slow = slow.next
    return True        



ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_true = LinkedList([1, 2, 3, 4, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))