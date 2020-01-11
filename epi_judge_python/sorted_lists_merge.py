from test_framework import generic_test

class ListNode:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node

# 7.1 Merge two sorted lists
# Write a program that takes two lists, assumed to be sorted,
# and returns their merge. The only field
# your program can change in a node is its next field.
def merge_two_sorted_lists(L1, L2):
    # SOS!!! Because we have no "pointers", we take a dummy node
    # just for using its "next"!!
    # SOS!!! dealing w/ the rest of the list:
    # tail.next = L1 or L2
    # don't forget to move the tail!! 
    dummy_head = tail = ListNode()
    while L1 and L2:
        # print(L1.data, L2.data, tail.data)
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    tail.next = L1 or L2
    
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
