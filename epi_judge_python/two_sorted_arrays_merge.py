from test_framework import generic_test

# 13.2 Merge two sorted arrays
# Write a Program which takes as input two sorted arrays of integers, and updates
# the first to the combined entries of the two arrays in sorted order. Assume the
# first array has enough empty entries at its end to hold the result.
# m and n are the number of entries initially in the first and second arrays
def merge_two_sorted_arrays(A, m, B, n):
    # SOS!!! what happens if one array is shorter than the other?
    idxA, idxB, write_idx = m - 1, n - 1, m + n - 1
    while idxB >= 0 and idxA >= 0:
        if A[idxA] <= B[idxB]:
            A[write_idx] = B[idxB]
            idxB, write_idx = idxB - 1, write_idx - 1
        else:
            A[write_idx] = A[idxA]
            idxA, write_idx = idxA - 1, write_idx - 1
    while idxB >= 0:
        A[write_idx] = B[idxB]
        idxB, write_idx = idxB - 1, write_idx - 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
