from test_framework import generic_test

# 4.8 Reverse Digits
# Write a program which takes an integer and returns the integer
# corresponding to the digits of the input written in reverse order.
# For example, the reverse of 42 is 24, and the reverse of -314 is -413
def reverse(x):
    # input may be negative, so take abs(x) for the beginning
    # mult successively w/ 10, not at once for each 10th power
    # we don't know anyway how log the x is
    nr = abs(x)
    res = 0
    while nr > 0 :
        res = nr % 10 + res * 10
        nr = nr // 10
    return -res if x < 0 else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
