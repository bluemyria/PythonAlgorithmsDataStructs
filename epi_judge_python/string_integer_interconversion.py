from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

# 6.1 Interconvert Strings and Integers
# Implement an integer to string conversion function, and a string to integer 
# conversion function. For example, if the input to the first function is the
# integer 314, it should retum the string "314" and if the input to the second
# function is the string "314" it should return the integer 314

# SOS!!! ord() function
# SOS string.digits
# SOS dealing w/ sign!!
def int_to_string(x):
    # TODO - you fill in here.
    if x == 0:
        return "0"
    lst = []
    sign_factor = -1 if x < 0 else 1
    x = x*sign_factor
    while x != 0:
        lst.append(chr(x%10 + ord('0')))
        x //= 10 
    if sign_factor == -1:
        lst.append('-')
    lst.reverse()
    s = "".join(lst)
    return s


def string_to_int(s):
    # TODO - you fill in here.
    l = len(s)
    sign = (-1 if l > 0 and s[0]=="-" else 1)
    return sign * sum((ord(s[i])-ord("0"))*10**(l-i-1) for i in range(len(s))
                   if s[i] in string.digits)


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    print(int_to_string(-0))
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
