from test_framework import generic_test
import heapq

# 10.5 Compute the median of online Data
# You want to compute the running median of a sequence of numbers. The sequence is presented to
# you in a streaming fashion-you carmot back up to read an earlier value, and you need to output
# the median after reading in each new element. 
# Design an algorithm for computing the running median of a sequence
def online_median(sequence):
    # Use one max and one min heap. they should have the same length if one is longer, only by one element!
    # (decide which one!)
    # they are only min_heaps in python, so do the trick w/ minus
    result = []
    min_h = []
    max_h = []
    for seq in sequence:
        heapq.heappush(max_h, -heapq.heappushpop(min_h, seq))
        if len(max_h) > len(min_h):
            heapq.heappush(min_h, -heapq.heappop(max_h))
        result.append( (min_h[0]-max_h[0])/2 if len(max_h) == len(min_h) else min_h[0] )

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
