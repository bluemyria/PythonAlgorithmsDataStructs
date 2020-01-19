from test_framework import generic_test

# 13.1 Compute the intersection of two sorted arrays
# Write a program which takes as hput two sorted arrays, and returns a new array containing
# elements that are present in both of the input arrays. The input arrays may have duplicate entries,
# but the returned array should be free of duplicates. For example, the input is <2,3,3,5,5,6,7,7,8,12>
# and (5,5,6,8 ,8,9,70,10), your output should be (5, 6, 8)
def intersect_two_sorted_arrays(A, B):
    # SOS!!! don't try to loop in the loop looking for duplicates!!
    # SOS!!! how do we check if the last one of an arry is sth? it may be non existent!?
    # see ln 16 
    res = []
    idxA, idxB = 0, 0
    while idxA < len(A) and idxB < len(B):
        if A[idxA] == B[idxB]:
            if len(res) == 0 or A[idxA] != res[-1]:
                res.append(A[idxA])
            idxA += 1
            idxB += 1
        elif A[idxA] < B[idxB]:
            idxA += 1
        else:
            idxB += 1   
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
