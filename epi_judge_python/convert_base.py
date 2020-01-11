from test_framework import generic_test
import string

# 6.2 Base Conversion
# Write a program that performs base conversion. The input is a string, 
# an integer b1, and another integer b2. The string represents an integer
# in base b1. The output should be the string representing the integer in
# base b2. Assume 2 < b1,b2 < 16. Use "A" to represent 10, "B" for 11,...,
# and "F" for 15. 
def convert_base(num_as_string, b1, b2):
    # SOS think if it is more convenient to reverse the "list" at the end
    l = len(num_as_string)
    s = num_as_string
    sign = (-1 if l > 0 and s[0]=="-" else 1)
    start = 0 if sign == 1 else 1 
    n = sum(string.hexdigits.index(s[i].lower())*b1**(l-i-1) for i in range(start,len(s)))

    lst = []
    while n != 0:
        lst.append( string.hexdigits[n%b2].upper() )
        n //= b2
    if lst == []:
        lst = ['0'] 
    if sign == -1:
        lst.append('-')
    lst.reverse()
    s = "".join(lst)
    return s 
    

if __name__ == '__main__':
    print(convert_base("1A",16,10))
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
