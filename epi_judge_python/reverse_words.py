import functools
import time

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# 6.6 Reverse all the words in a sentence
# Assume s is a string encoded as bytearray.
def reverse_words(s):
    def reverse_single_word(l,r):
        while l < r:
            s[l], s[r] = s[r], s[l] 
            l , r = l+1, r-1

    # SOS!!! Bytearray!! Otherwise cannot reverse()!
    # SOS!!! why reverse the whole sentence?
    # SOS!!! with the limits of the words!
    # what happens w/ the last word?
    s.reverse()
    start = 0
    while True:
        end_word = s.find(b" ",start)
        if end_word < 0:
            break
        reverse_single_word(start, end_word-1)
        start = end_word + 1
        # print(s)
    reverse_single_word(start, len(s)-1)
    # print(s)   
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")

    
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
