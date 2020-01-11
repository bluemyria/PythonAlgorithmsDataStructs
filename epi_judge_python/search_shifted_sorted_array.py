from test_framework import generic_test

# 11.3 Search a cyclically Sorted Array
# Design art O(logn) algorithm for finding the position of the smallest element in a 
# cyclically sorted array. Assume all elements are distinct. 
def search_smallest(A):
    left, right = 0 , len(A)-1

    while left < right:
        mid = (left + right)//2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
