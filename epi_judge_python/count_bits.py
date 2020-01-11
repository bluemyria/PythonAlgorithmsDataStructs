from test_framework import generic_test

# 4.0 Count the number of bits that are set to 1 in a positive integer
def count_bits(x):
    # SOS!!! x & x-1 gets rid of the last set bit (1) of x !!
    nr = 0
    while x > 0:
        x &= x-1
        nr += 1
    return nr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
