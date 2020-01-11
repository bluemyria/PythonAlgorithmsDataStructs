import random
from test_framework import generic_test

# 11.8 Find the k-th largest element
# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def partition_around_pivot(left, right, pivot_idx):
        # The coding is for pivot partitioning
        # SOS!!!!! The pivor is outside of the emlements being shifted!!!!
        # it takes its final place at the end!!!
        pvt_value = A[pivot_idx]
        A[pivot_idx], A[right] = A[right], A[pivot_idx]
        new_pvt_idx = left
        # pivor "sits" on the right edge, ie it doesnot get moved
        for i in range (left, right):
            # we are ordering all largest on the left!!!!!!!!
            if A[i] > pvt_value:
                A[i], A[new_pvt_idx] = A[new_pvt_idx], A[i]
                new_pvt_idx += 1
        # pivot gets its final position
        A[new_pvt_idx], A[right] = A[right], A[new_pvt_idx]
        return new_pvt_idx


    left, right = 0, len(A)-1
    while left <= right:
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            right = new_pivot_idx - 1
        else:
            left = new_pivot_idx + 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
