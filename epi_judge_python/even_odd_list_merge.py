from test_framework import generic_test

class ListNode:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node

# 7.10 Implement Even-Odd Merge
# Consider a singly linked list whose nodes are numbered starting at 0. Define the even-odd merge of
# the list to be the list consisting of the even-numbered nodes followed by the odd-numbered nodes.
def even_odd_merge(L):
    # dummy_head a good way to start
    # think of how to connect the even end w/ the odd start
    dummy_head = ListNode(0, L)

    if dummy_head.next and dummy_head.next.next:
        etail = erun = dummy_head.next
        otail = orun = o = dummy_head.next.next
    else:
        return L
    eready = oready = False
    while not oready or not eready:
        if etail.next and etail.next.next:
            erun = etail.next.next
            etail.next = erun
            etail = erun
        else:
            eready = True
        if otail.next and otail.next.next:
            orun = otail.next.next
            otail.next = orun
            otail = orun
        else:
            oready = True
    erun.next = o
    orun.next = None
    return dummy_head.next    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
