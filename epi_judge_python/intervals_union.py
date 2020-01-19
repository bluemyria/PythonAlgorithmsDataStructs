import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

# 13.7 Compute the union of intervals
# In this problem we consider sets of intervals with integer endpoints; the intervals may be open
# or closed at either end. We want to compute the union of the intervals in such sets
# Design an algorithm that takes as input a set of intervals, and outputs their union expressed as a
# set of disjoint intervals.
# Input:
# array(tuple(int[left value], bool[left is closed], int[right value], bool[right is closed]))
# [[610, false, 613, true], [204, true, 205, true]]
def union_of_intervals(intervals):
    if not intervals:
        return []

    # sort by left endpoint starting first, closed endpoint first 
    intervals.sort(key = lambda x: (x.left.val, not x.left.is_closed))
    union_intervals = [intervals[0]]

    for itv in intervals:
        last_added = union_intervals[-1]
        
        #print("___start intervals___")
        #print(itv.left.val, itv.left.is_closed, itv.right.val, itv.right.is_closed)
        #print(last_added.left.val, last_added.left.is_closed, last_added.right.val, last_added.right.is_closed)
        if (itv.left.val > last_added.right.val):
            union_intervals.append(itv)
        elif (itv.left.val < last_added.right.val and
              itv.right.val > last_added.right.val):
            last_added = Interval(last_added.left, itv.right)
            union_intervals[-1] = last_added
        elif itv.left.val == last_added.right.val:
            if (itv.left.is_closed == True or last_added.right.is_closed == True):
                last_added = Interval(last_added.left, itv.right)
                union_intervals[-1] = last_added
            else:
                union_intervals.append(itv)
        elif (itv.right.val == last_added.right.val and
              last_added.right.is_closed == False and itv.right.is_closed == True):
            last_added = Interval(last_added.left, itv.right)
            union_intervals[-1] = last_added
        #print("result",union_intervals[-1].left.val, union_intervals[-1].left.is_closed, union_intervals[-1].right.val, union_intervals[-1].right.is_closed)

    return union_intervals


# print(union_of_intervals([[8, True, 9, False], [157, False, 166, False], [163, False, 168, True], [177, True, 182, True], [30, True, 32, False], [169, False, 170, True], [149, True, 153, False], [121, False, 129, False], [226, False, 228, False], [211, False, 217, True], [177, True, 184, False], [8, False, 17, True], [225, True, 233, True], [16, True, 18, False], [243, False, 246, False], [102, True, 110, True], [170, True, 173, True], [169, True, 175, True], [169, False, 170, True], [105, True, 108, False], [125, False, 128, False], [61, True, 67, False], [175, False, 180, False], [205, True, 210, False], [125, False, 128, False]]	))
# [[8, True, 18, False], [30, True, 32, False], [61, True, 67, False], [102, True, 110, True], [121, False, 129, False], [149, True, 153, False], [157, False, 168, True], [169, True, 184, False], [205, True, 210, False], [211, False, 217, True], [225, True, 233, True], [243, False, 246, False]]



@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
