import unittest

def char_reverse(list_of_chars):
    left_index = 0
    right_index = len(list_of_chars) - 1
    print(list_of_chars)

    while left_index < right_index:
        list_of_chars[right_index], list_of_chars[left_index] = list_of_chars[left_index], list_of_chars[right_index]
        right_index -= 1
        left_index += 1
    print(list_of_chars)
    return list_of_chars


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ("1 2 3 4 5 6 7 8 9".split(),"9 8 7 6 5 4 3 2 1".split()),
        ("".split(),"".split()),
        ("a".split(),"a".split()),
        ("a a a a a a b b b".split(),"b b b a a a a a a".split()),
        ("1 2 3 4".split(),"4 3 2 1".split()),
    ]

    def test_reverse(self):
        for test_array, expected in self.data:
            actual = char_reverse(test_array)
            print(actual)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()


