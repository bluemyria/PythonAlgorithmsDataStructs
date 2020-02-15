import collections

from test_framework import generic_test

# 18.2. Paint a Boolean matrix
# Implement a routine that takes an n x m Boolean anay A together with 
# an entry (r, g) ana flips the color of the region associated with (x, y). 
def flip_color(x, y, image):
    color = image[x][y]
    dq = collections.deque([(x,y)])
    image[x][y] = 1-image[x][y]
    while dq:
        m, n = dq.popleft()
        for xnext, ynext in [(m-1,n),(m+1,n),(m,n-1),(m,n+1)]:
            if ( 0 <= xnext < len(image) and
                 0 <= ynext < len(image[0]) and
                 image[xnext][ynext] == color ):
                image[xnext][ynext] = 1 - image[xnext][ynext]
                dq.append((xnext,ynext))


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
