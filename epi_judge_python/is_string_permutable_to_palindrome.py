from test_framework import generic_test
import collections

# 12.1 Test for palindromic permutations
def can_form_palindrome(s):
    # SOS!!! collections.Counter can take a string as an arg and counts the chars then!
    # SOS!!! don't forget to use the values() of the Counter
    return sum(v%2 for v in collections.Counter(s).values()) <= 1 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
