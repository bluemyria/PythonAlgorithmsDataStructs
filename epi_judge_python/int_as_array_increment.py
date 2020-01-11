from test_framework import generic_test

# 5.2 Increment an arbitrary-precision Integer
# Write a program which takes as input an array of digits encoding a 
# nonnegative decimal integer D and updates the array to represent 
# the integer D + 1. For example, if the input is (1,2,9) then
# you should update the array to (1,3,0). Your algorithm should work even
# if it is implemented in a language that has finite-precision arithmetic.
def plus_one(A):
    # better add one and check if it is 10 than just checking if it is 9??
    l = len(A)
    if l == 0:
        return [1] 
    carrier = 1
    for i in range(l-1, -1, -1):
        A[i] += carrier
        if A[i] == 10:
            carrier = 1
            A[i] = 0
        else:
            carrier = 0
            break
    if carrier == 1:
        A.insert(0,1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
