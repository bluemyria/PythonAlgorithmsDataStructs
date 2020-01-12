from test_framework import generic_test
import collections

# 12.5 Find the nearest repeated entries in an array
# return -1 of no repetitions
def find_nearest_repetition(paragraph):
    # SOS!!! revise defaultdict functions!!
    last_occurance_of_word = collections.defaultdict(None)
    nearest_repetition = len(paragraph) + 1
    for i, w in enumerate(paragraph):
        if w in last_occurance_of_word:
            last_position = last_occurance_of_word[w]
            if i - last_position < nearest_repetition :
                nearest_repetition = i - last_position
        last_occurance_of_word[w] = i
    return nearest_repetition if nearest_repetition <= len(paragraph) else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
