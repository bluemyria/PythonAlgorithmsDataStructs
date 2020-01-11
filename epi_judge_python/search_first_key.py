from test_framework import generic_test

# 11.1 Search Sorted Array for first occurence of k
# Write a method that takes a sorted array and a key and retums the index
# of the first occurrence of that key in the array. Return -1
# if the key does not appear in the array. 
def search_first_of_k(A, k):
    # SOS!!! calc the mid one! 
    # SOS!!! not causing endless loops
    left, right, result = 0, len(A)-1, -1

    while left <= right:
        mid = (left + right)//2
        if A[mid] > k: 
            right = mid - 1
        elif A[mid] < k:
            left = mid + 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
