from test_framework import generic_test

class ListNode:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node
        
# 7.7 Remove the Kth last element from a List
# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # SOS!!!!!
    # everything was good until the last kth element was the head!!!!!!!!!!!
    # MUST use a dummy_head and start w/ it!!!!!
    if not L:
        return None
    dummy_head = ListNode(0, L)
    f = s = dummy_head
    for _ in range(k):
        s = s.next
    while s and s.next:
        f, s = f.next, s.next
    f.next = f.next.next    
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
