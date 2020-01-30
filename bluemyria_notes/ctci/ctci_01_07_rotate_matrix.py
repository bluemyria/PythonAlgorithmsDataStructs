import unittest

def rotate_matrix_2matr(ma):
    n = len(ma[0])
    m = [ [ 0 for i in range(n) ] for j in range(n) ] 
    for i in range(n):
        for j in range(n):
            # print(i, j, n-j-1, i)
            m[i][j] = ma[n-j-1][i]
    return m

# try to solve it w/ only one martix
def rotate_matrix(ma):
    n = len(ma)
    start = 0
    end = n
    print( ma[0][1], ma[2][0]) 
    for x in range(0, n//2):
        print("x",x)
        for y in range(start, end-1):
            print("y",y)
            print("prin", ma[y][x], ma[n-x-1][y], ma[n-y-1][n-x-1], ma[x][n-y-1])

            help = ma[y][x]
            ma[y][x] = ma[n-x-1][y]
            ma[n-x-1][y] = ma[n-y-1][n-x-1]
            ma[n-y-1][n-x-1] = ma[x][n-y-1]
            ma[x][n-y-1] = help
            
            print("meta", ma[y][x], ma[n-x-1][y], ma[n-y-1][n-x-1], ma[x][n-y-1])

        start += 1
        end -= 1
    print(ma[0],ma[1],ma[2],ma[3],ma[4])
    return ma

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
