import unittest

def str_compression(s):
    if s =="":
        return s
    
    str_list=[]
    base_ch = s[0]
    base_i = 1
    for ch in s[1:]:
        if ch == base_ch:
            base_i += 1
        else:
            str_list.append(base_ch)
            str_list.append(str(base_i))
            base_ch = ch
            base_i = 1
    str_list.append(base_ch)
    str_list.append(str(base_i))

    s_new = "".join(str_list)
    return s_new if len(s_new) < len(s) else s

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('dddtstttttazzz', 'd3t1s1t5a1z3'),
        ('', ''),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = str_compression(test_string)
            print(test_string, actual, expected)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()    