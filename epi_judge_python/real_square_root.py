import math
from test_framework import generic_test

# 11.5 Compute the real square root
# Implement a function which takes as input a floating point value and returns
# its square root.
# Hint: Iteratively compute a sequence of intervals, each contained in the previous
# interval, that contain the result.
def square_root(x):
    # think of the case the float is smaller than 1!
    # SOS usage of math.isclose()!!
    (left, right) = (1.0, x) if x >= 1 else (x, 1.0)
    while not math.isclose(left, right):
        mid = (left+right)/2.0
        if mid*mid > x:
            right = mid
        else:
            left = mid
    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
