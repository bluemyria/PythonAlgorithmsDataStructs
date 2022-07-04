import unittest

def order_checker(list1, list2, list3):
    
    idx1, idx2 = 0, 0
    
    # check that all orders of list3 are from list1 and list2 and in order
    for order in list3:
        if idx1 < len(list1) and list1[idx1] == order:
            idx1 += 1
        elif idx2 < len(list2) and list2[idx2] == order:
            idx2 += 1
        else:
            return False

    # check that no orders of list1 or list2 we left unserved (not included in list3)
    if idx1 < len(list1) or idx2 < len(list2):
        return False

    return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([1, 3, 5],
        [2, 4, 6],
        [1, 2, 4, 6, 5, 3],
        False),
        ([17, 8, 24],
        [12, 19, 2],
        [17, 8, 12, 19, 24, 2],
        True),
        ([17, 8, 24, 5, 7],
        [12, 19, 2],
        [17, 8, 12, 19, 24, 2],
        False),
        ([1],
        [],
        [1],
        True),
        ([],
        [],
        [],
        True),
    ]

    def test_order_checker(self):
        for test_array1, test_array2, test_array3, expected in self.data:
            actual = order_checker(test_array1, test_array2, test_array3)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()


