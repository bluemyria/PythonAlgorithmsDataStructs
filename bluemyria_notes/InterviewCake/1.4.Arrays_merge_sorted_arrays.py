import unittest

def merge_sorted_arrays(list1, list2):
    
    sorted_list = []
    idx1, idx2 = 0, 0
    
    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] <= list2[idx2]:
            sorted_list.append(list1[idx1])
            idx1 += 1
        else:
            sorted_list.append(list2[idx2])
            idx2 += 1
    while idx1 < len(list1):
        sorted_list.append(list1[idx1])
        idx1 += 1
    while idx2 < len(list2):
        sorted_list.append(list2[idx2])
        idx2 += 1
    
    return sorted_list


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([3, 4, 6, 10, 11, 15],
        [1, 5, 8, 12, 14, 19],
        [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]),
        ([3, 4, 6],
        [],
        [3, 4, 6]),
        ([],
        [],
        []),
    ]

    def test_merge_sorted_arrays(self):
        for test_array1, test_array2, expected in self.data:
            actual = merge_sorted_arrays(test_array1, test_array2)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()


