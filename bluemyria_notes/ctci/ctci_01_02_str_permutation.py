# O(N)
import unittest

def check_permutation(str1,str2):
    #assuming ascii chars
    if len(str1) != len(str2):
        return False
    a = [ch for ch in str1]
    a.sort()    #  
    b = [ch for ch in str2]
    b.sort()    # SOS!!!! sort() gives None as return Value!!!! never assign to sth!!!
    
    for (ch1,ch2) in zip(a,b):
        if ch1 != ch2:
            return False
    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
