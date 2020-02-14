from test_framework import generic_test

# 5.18 Compute the spiral ordering of a 2D Array
def matrix_in_spiral_order(square_matrix):
    # SOS!!! the square in the middle of the matrix is still missing if n -> odd 
    # SOS!! for summerty think of where to stop the line...
    mso = []
    #print("\n_____________________________________________________")
    #print(square_matrix)
    n = len(square_matrix)
    if n == 1:
        return square_matrix[0]
    start = 0
    end = n-1
    while end > start:
        for i in range(start, end):
            mso.append(square_matrix[start][i])
        for i in range(start, end):
            mso.append(square_matrix[i][end])
        for i in range(end, start, -1):
            mso.append(square_matrix[end][i])
        for i in range(end, start, -1):
            mso.append(square_matrix[i][start])
        start += 1
        end -= 1
        print(start, end)

    # the square in the middle of the matrix is still missing if n -> odd 
    if n%2 == 1:
        mso.append(square_matrix[start][end])        
    #print(mso)
    return mso


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
