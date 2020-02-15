from test_framework import generic_test

# 17.7 Compute the maximum water trapped by a pair of vertical lines
def get_max_trapped_water(heights):
    max_water = 0
    l, r = 0, len(heights)-1
    while l < r:
        max_water = max(max_water, min(heights[l], heights[r])*(r-l))
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1             
    return max_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
