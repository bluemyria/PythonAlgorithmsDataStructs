from test_framework import generic_test

class ListNode:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node

# 7.2 Reverse a single sublist
# Write a program which takes a singly linked list L and two integers
# s and f as arguments, and reverses the order of the nodes from the
# sth node to fth node, inclusive. The numbering begins at 1., i.e.,
# the head node is the first node. Do not allocate additional nodes
# (but you may allocate additional nodes as "pointers" -  my remark)
def reverse_sublist(L, s, f):
    # SOS!!! check empty lists, s, f limits
    #  

    if not L:
        return None
    if f-s <= 0:
        return L
    dummy_head = head_sub_lst = ListNode(0, L)
    
    # head_sub_lst points to last node before revlst
    # paint pointers very carefully!! check NONE!!!!
    # there is another solution w/o last.. in the book. check it
    for _ in range(1, s):
        head_sub_lst = head_sub_lst.next
    iter_sub_lst = head_sub_lst.next
    inext = iter_sub_lst.next
    last = iter_sub_lst
    for _ in range(s, f):
        end = iter_sub_lst
        head_sub_lst.next = inext
        inext = inext.next
        iter_sub_lst = head_sub_lst.next
        iter_sub_lst.next = end
    last.next = inext
    return dummy_head.next
    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
