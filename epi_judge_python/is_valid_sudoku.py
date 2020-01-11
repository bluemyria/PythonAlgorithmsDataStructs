from test_framework import generic_test
import math

# 5.17 The Sudoku checker Problem
# Check whether a 9x9 2D arcay representing a partially completed Sudoku
# is valid. Specifically, check that no row, column, or 3 x 3 2D subarray
# contains duplicates. A O-value in the 2D array indicates that entry is
# blank; every other entry is in [1,9].

# SOS!!!!!
# The expression for choosing all columns is very important!!!
#  b = [ [a[j][i] for j in range(n)] for i in range(n)]
# to refresh your memory: check:
# print([ [ (j,i) for j in range(5)] for i in range(5)])


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    # Use a instead of partial_assignment => shorter
    a = partial_assignment
    is_valid = rows_are_valid(a) & columns_are_valid(a) & little_squares_are_valid(a)
    return is_valid


def rows_are_valid(a):
    return all([has_no_dup(row) for row in a])


def columns_are_valid(a):
    n = len(a)
    b = [ [a[j][i] for j in range(n)] for i in range(n)]
    return all([has_no_dup(row) for row in b])


def little_squares_are_valid(a):
    d = []
    sr = int(math.sqrt(len(a)))
    for i in range(0, sr):
        for j in range(0, sr):
            # First Solution without list comprehensions
            # c = []
            # for k in range(0, sr):
            #     for l in range(0, sr):
            #         c.append(a[i*sr+k][j*sr+l])
            # b.append(c)
            d.append([ a[i*sr+k][j*sr+l] for k in range(sr) for l in range(sr)])
    return all([has_no_dup(row) for row in d])


def has_no_dup(a):
    no_zeroes = [x for x in a if x!=0]
    return len(no_zeroes) == len(set(no_zeroes))

print(has_no_dup([1,4,7,5,4,5,4,5,0,0,0,0,9]))

print(has_no_dup([1,4,0,0,0,0,5,8]))

 
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
