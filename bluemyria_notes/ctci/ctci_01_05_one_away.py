import unittest

def one_away(s1, s2):
    if len(s1)==len(s2):
        return check_edit(s1, s2)
    elif len(s1)+1 == len(s2):
        return check_add(s1, s2)
    elif len(s1) == len(s2)+1:
        return check_add(s2,s1)
    else:
        return False

def check_edit(s1,s2):
    diff = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            diff += 1
    return diff <= 1


def check_add(s1, s2):
    diff = 0
    for i, ch in enumerate(s1):
        if ch != s2[i+diff]:
            diff += 1
            if ch != s2[i+diff]:
                return False
    return False if diff > 1 else True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            print(test_s1, test_s2, actual, expected)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()