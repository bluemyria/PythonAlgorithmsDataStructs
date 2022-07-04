import unittest

def bracket_validator(code):
    openers = [ '(', '{', '[' ] 
    closers = [ ')', '}', ']']
    br_stack = []
    for ch in code:
        if ch in openers:
            br_stack.append(ch)
        else:
            if ch in closers:
                if not len(br_stack) or closers.index(ch) != openers.index(br_stack.pop()):
                    return False
    return False if len(br_stack) else True
                


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ( "{ [ ] ( ) }", True),
        ( "{ [ ] ) ) ) ) }", False),
        ( "{ [ { ( ( ( ) ) ) } ] ( ) }", True),
        ( "{ [ [ [ [ ] ( ) ( ) { } }", False),
        ( "{ [ ( ] ) }", False),
        ( "{ [ }", False)
    ]

    def test_order_checker(self):
        for test_array, expected in self.data:
            actual = bracket_validator(test_array)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
    
