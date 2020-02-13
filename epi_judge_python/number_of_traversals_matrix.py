
from test_framework import generic_test

# 16.3 Count the number of ways to traverse a 2D array
def number_of_ways(n, m):
    def calc_nr_of_ways(a, b):
        if a == b == 0:
            return 1
        if nr_of_ways[a][b] == 0:
            ways_from_top = 0 if a == 0 else calc_nr_of_ways(a - 1, b)
            ways_from_left = 0 if b == 0 else calc_nr_of_ways(a, b - 1)
            nr_of_ways[a][b] = ways_from_top + ways_from_left
        return nr_of_ways[a][b]

    nr_of_ways = [[0] * m for _ in range(n)]
    return calc_nr_of_ways(n - 1, m - 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
