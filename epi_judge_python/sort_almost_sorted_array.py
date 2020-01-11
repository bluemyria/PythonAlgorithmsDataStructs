from test_framework import generic_test
import heapq, itertools

# 10.3 Sort an almost sorted aaray
# Write a Program which takes as input a very long sequence of numbers and prints the numbers in
# sorted order. Each number is at most k away from its correctly sorted position. (Such an array is
# sometimes referred to as being k-sorted.) 
# Hint: How many numbers must you read after reading the ith number to be sure you can place it
# in the correct location
def sort_approximately_sorted_array(sequence, k):
    result = []
    min_heap = []

    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)
    
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
