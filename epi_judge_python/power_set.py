import math

from test_framework import generic_test, test_utils

# 15.4 Generate the power set
def generate_power_set(S):
    # SOS, create for eg size 5, all combinations 00000, 00001, ...., 11110, 11111
    result = []
    # 1 << len(S) gives 100000 for len(S) == 5
    for int_for_subset in range(1 << len(S)):
        subset = []
        bit_array = int_for_subset
        while bit_array:
            # add to array only nrs that correspond to an 1 in bit_array
            # bit_array & ~(bit_array-1) isolates the lowest bit
            subset.append(int(math.log2(bit_array & ~(bit_array-1))))
            # bit_array & (bit_array-1) gets rid of the lowest bit
            bit_array &= bit_array - 1 
        result.append(subset)
    
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
