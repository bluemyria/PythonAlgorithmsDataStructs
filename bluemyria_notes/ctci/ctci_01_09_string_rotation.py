import unittest

def str_rotation(s_orig,s_rot):
    if (len(s_orig) == len(s_rot)):
        return is_substring(s_rot*2,s_orig)
    return False

def is_substring(string, sub):
    return string.find(sub) != -1     

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = str_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()