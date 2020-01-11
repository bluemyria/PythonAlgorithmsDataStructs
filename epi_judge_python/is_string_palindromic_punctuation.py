from test_framework import generic_test
import string

# 6.5 Test Palindromicity

#For the purpose of this problem, define a palindromic string to be a string which when all the
# non-alphanumeric are removed it reads the same front to back ignoring case. For example, "A man,
# a plan, a canal/ Panama." and "Able was I, ere I saw Elba!" are palindromic, but "Ray a Ray" is not.
# Implement a function which takes as input a string s and retums true if s is a palindromic string.
def is_palindrome(s):
    # SOS!!! non-alphanumeric must be ignored! not non-letters!!
    # SOS!!! upper, lower checks!
    palindrome = True
    l , r = 0, len(s) - 1
    while l < r:
        while not (s[l] in string.ascii_letters or s[l] in string.digits) and l < r:
            l += 1
        while not (s[r] in string.ascii_letters or s[r] in string.digits) and l < r:
            r -= 1
        if s[l].lower() != s[r].lower():
            palindrome = False
            break
        l += 1
        r -= 1
        
    return palindrome


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
