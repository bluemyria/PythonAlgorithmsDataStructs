import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 7.4 Tests for overlapping Lists-Lists are cycle-free
# Write a Program that takes two cycle-free singly linked lists, 
# and determines if there exists a node that is common to both lists.
def overlapping_no_cycle_lists(l0, l1):
    # SOS!!!!!!
    # I took l1, l2 instead of l0, l1 :(
    # I checked if l0 = l1  !!!!!!!!!!!!!!!!!!!!!!!
    # instead of if l0 == l1  :(   :(   :(
    len0 = len1 = 0
    head0, head1 = l0, l1
    
    while l0 and l0.next:
        len0 += 1
        l0 = l0.next
    
    
    while l1 and l1.next:
        len1 += 1
        l1 = l1.next

    l0, l1 = head0, head1
    
    if len0 > len1:
        for _ in range(len0-len1):
            l0 = l0.next  
    
    if len1 > len0:
        for _ in range(len1-len0):
            l1 = l1.next  
    
    while l0 and l1 and l0 != l1:
        l0, l1 = l0.next, l1.next
    
    if l0 == l1:
        return l0
    else:
        return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
