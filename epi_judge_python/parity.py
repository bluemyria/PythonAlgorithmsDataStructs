from test_framework import generic_test

# 4.1 Compute the parity of a word
# ∃ Brute force:
# a_parity is better (counts only the ones)
# there is a better solution with a lookup table
# even shorter: parity via xor w/ the other half

# SOS: same effect
# par = not par
# par ^= 1

def a_parity(x):
    # TODO - you fill in here.
    par = 0
    while x > 0:
        x &= x -1
        # par = not par
        par ^= 1

    return par

def parity(x):
    # TODO - you fill in here.
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1 


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
