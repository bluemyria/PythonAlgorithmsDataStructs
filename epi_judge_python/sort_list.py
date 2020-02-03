from test_framework import generic_test
from sorted_lists_merge import merge_two_sorted_lists

# 13.10 Implement a fast sorting algorithm for lists
# Implement a routine which sorts lists efficiently. It should be a stable sort, i.e., the relative positions
# of equal elements must remain unchanged.
def stable_sort_list(L):
    if not L or not L.next:
        return L
    prev_slow, slow, fast = None, L, L
    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    prev_slow.next = None
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
