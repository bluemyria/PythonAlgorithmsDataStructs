from test_framework import generic_test

# 17. Greedy Algorithms BootCamp
def has_two_sum(A, t):
    return any( t-x in A for x in A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
