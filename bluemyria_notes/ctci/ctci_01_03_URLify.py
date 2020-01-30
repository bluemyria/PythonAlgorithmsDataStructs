# O(N)
import unittest

def urlify(s,l):
    if " " not in s:
        return s
    
    s_help = s.strip()
    wl = s_help.split(" ")
    return "%20".join(wl)



class Test(unittest.TestCase):
    """Test Cases"""
    data = [
        ('much ado about nothing      ', 28,
         'much%20ado%20about%20nothing'),
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
