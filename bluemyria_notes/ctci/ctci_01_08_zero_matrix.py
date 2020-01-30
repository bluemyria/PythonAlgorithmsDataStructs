import unittest

def zero_matrix(ma):
    x = len(ma)
    y = len(ma[0])
    x_zero = []
    y_zero = []

    for i in range(x):
        for j in range(y):
            if ma[i][j] == 0:
                x_zero.append(i)
                y_zero.append(j)

    for i in x_zero:
        for k in range(x):
            ma[i][k] = 0


    for j in y_zero:
        for k in range(y):
            ma[k][j] = 0

    return ma



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()    