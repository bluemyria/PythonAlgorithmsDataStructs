import unittest


def pal_perm(s):

    counter = [0 for i in range(ord('Z')-ord('A')+1)]
    numchars = 0
    
    for ch in s:
        i = char2num(ch)
        if i == -1:
            continue
        counter[i] = counter[i] + 1
        numchars += 1
    
    numodd = 0
    for k in counter:
        numodd += k%2
    
    if numchars%2 == 1 and numodd > 1:
        return False
    if numchars%2 == 0 and numodd > 0:
        return False
    return True

def char2num(c):
    if ( ord('a') <= ord(c) <= ord('z') ) :
        return ord(c)-ord('a')
    if ( ord('A') <= ord(c) <= ord('Z') ) :
        return ord(c)-ord('A')
    else:
        return -1

pal_perm('nipsonanomimatamimonanopsin')


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()