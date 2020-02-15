from test_framework import generic_test

# 17.4 The 3-sum problem
# Design an algorithm that takes as input an array and a number, and determines
# if there are three entries in the array (not necessarily distinct) which add up
# to the specified number
def has_three_sum(A, t):
    def has_two_sum(A, t):
        return any( t-x in A for x in A)
    
    return any( has_two_sum(A, t-x) for x in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
