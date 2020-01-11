from test_framework import generic_test
from test_framework.test_failure import TestFailure
import itertools

# 11.9 Find the missing IP address
def find_missing_element(stream):
    # too crazy to code
    # copied from the book, read it!!!!
    NUM_BUCKET = 1<<16
    counter = [0] * NUM_BUCKET
    stream, stream_copy = itertools.tee(stream)
    
    for x in stream:
        upper_part_x = x >> 16
        counter[upper_part_x] += 1
        # Look for a bucket that contains less than (1 << 16) elements
        BUCKET_CAPACITY = 1 << 16
        candidate_bucket = next(i for i, c in enumerate(counter)
                                if c < BUCKET_CAPACITY)
        # Finds all IP addresses in the stream whose first 16 bits are equal to
        # candidate-bucket.
        candidates = [0] * BUCKET_CAPACITY
        stream = stream_copy
        for x in stream_copy:
            upper_part_x = x >> 16
            if candidate_bucket == upper_part_x:
                # Records the presence of 16 LSB of x.
                lower_part_x = ((1 << 16) - 1) & x
                candidates[lower_part_x] = 1
        # At least one of the LSB conbinations is absent
        # find it
        for i, v in enumerate(candidates):
            if v == 0:
                return (candidate_bucket << 16) | i


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
