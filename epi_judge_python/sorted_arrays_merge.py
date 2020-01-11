from test_framework import generic_test
import heapq
import collections
# 10.1 Merge Sorted Files
# Write a program that takes as input a set of sorted sequences and computes the union of these
# sequences as a sorted sequence. 
def merge_sorted_arrays(sorted_arrays):
    # SOS!!! Sequences are already sorted. Put the first ones from each sequence in a min_heap
    # pop the smallest, put it in result array. Replace the smallest from the next one from
    # the same array
    # SOS!!! the usage of iterators!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # lines: 16, 18-19, 26-27  

    # pythonic solution
    # return list(heapq.merge(*sorted_arrays))
    # SOS!!! heapq.merge(*iterables) merges multiple sorted inputs into a single sorted output
    # (for example, merge timestamped entries from multiple log files).
    # Returns an iterator over the sorted values!!

    result = []
    min_heap = []
    arr_iters = [iter(arr) for arr in sorted_arrays]
    
    for i, it in enumerate(arr_iters):
        elem = next(it, None)
        if elem is not None:
            heapq.heappush(min_heap, (elem, i))

    while min_heap:
        smallest_elem, smallest_array = heapq.heappop(min_heap)
        result.append(smallest_elem)
        elem = next(arr_iters[smallest_array], None)
        if elem is not None:
            heapq.heappush(min_heap, (elem, smallest_array))
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
