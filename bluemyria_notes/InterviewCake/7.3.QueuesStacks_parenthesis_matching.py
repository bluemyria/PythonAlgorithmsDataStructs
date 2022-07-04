import unittest

def get_closing_paren(sentence, opening_paren_index):
    open_br = 1
    if len(sentence) < opening_paren_index or sentence[opening_paren_index] != '(':
        return -1
    for i,ch in enumerate(sentence[opening_paren_index+1:]):
        # print(i,ch, open_br)
        if ch == '(':
            open_br += 1 
        elif ch == ')':
            open_br -= 1
            if open_br == 0:
                return i + opening_paren_index + 1          
    return -1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ( "Some (when (my) too much (like  (and ))) they", 5, 39),
        ( " (when (my ()()()(((())))) too much ((((((((((like this (and this))) they get confusing", 1, -1),
        ( "(()((()))()()())", 0, 15)
    ]

    def test_order_checker(self):
        for test_array, idx, expected in self.data:
            actual = get_closing_paren(test_array, idx)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
    
