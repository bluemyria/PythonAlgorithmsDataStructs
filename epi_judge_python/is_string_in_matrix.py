from test_framework import generic_test

# 16.5 Search for a sequence in a 2D array
def is_pattern_contained_in_grid(grid, S):
    
    def is_pattern_suffix_contained_starting_at_xy(x, y, offset):
        if offset == len(S):
            return True
        
        if (0 <= x < len(grid) and  0 <= y < len(grid[x])
            and grid[x][y] == S[offset]
            and (x, y, offset) not in checked 
            and any (
                is_pattern_suffix_contained_starting_at_xy(a, b, offset+1)
                for (a, b) in ((x-1, y), (x, y-1), (x+1, y), (x, y+1)))):
            return True
        checked.add((x, y, offset))
        return False
        
    checked = set()
    return any(
        is_pattern_suffix_contained_starting_at_xy(i, j, 0)
        for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
