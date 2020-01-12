from test_framework import generic_test
import collections

# 12.4 Is an anonymous letter constructible?
# SOS!!! consider what happens when one dict is substracted from the other!
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    return not collections.Counter(letter_text)-collections.Counter(magazine_text)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
