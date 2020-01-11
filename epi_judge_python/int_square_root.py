from test_framework import generic_test

# 11.4 Compute the Integer Square Root
# Write a program which takes a nonnegative integer and returns the largest integer
# whose square is less than or equal to the given integer.
# Hint: Look out for a comer-case.
def square_root(k):
    # try to understand why left <= right or left < right
    # try to understand why left = mid + 1 or left = mid 
    # try to understand why right = mid - 1 or right = mid
    # try to understand why return left -1
    left, right = 0, k
    while left <= right:
        mid = (left + right)//2
        if mid**2 <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
