from test_framework import generic_test

# 4.3 Reverse bits
# Write a program that takes a 64-bit unsigned integer and returns
# the 64-bit unsigned integer consisting of the bits of the input
# in reverse order. For example, if the input is (1110000000000001),
# the output should be (1000000000000111).
def reverse_bits(x):
    # SOS!!! x xor 1 reverses the bit
    # check bit in position i:
    # x >> i & 1  it isolates the bit
    for i in range(32):
        if ((x >> i) & 1 ) ^ ((x >> (63-i)) & 1 ):
            bit_mask = 1 << i | 1 << 63-i
            x = x ^ bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
