# O(N)
import unittest

def has_unique_chars(string):
    #assuming ascii chars
    if len(string) > 128:
        return False
    
    char_set = [False for ch in range(128)]
    for ch in string:
        i = ord(ch)
        if char_set[i]:
            return False
        else:
            char_set[i] = True
    return True

def has_unique_chars2(string):
    #assuming ascii chars   ####   BITWISE OPERATORS!!!!
    if len(string) > 128:
        return False
    
    checker = 0
    print(checker)
    for ch in string:
        i = ord(ch)
        if checker & (1 << i):
            print(i, ch, "False", checker)
            return False
        else:
            checker = checker | (1 << i)
            print(i, ch, "True", checker)
    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()'), ('sdkjf haskdjfh alskdjfh alskjfdh laskjdfh alskjdfhlaskjdfh alskdjfh laksjdfh laskjdfh alskjdfhlkj halsdkjf haslkdjfh alskjdfh laksjdfh alskdjfh alskdjfh laskjdfh alskjdfh laksdjfh la')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = has_unique_chars2(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = has_unique_chars2(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
