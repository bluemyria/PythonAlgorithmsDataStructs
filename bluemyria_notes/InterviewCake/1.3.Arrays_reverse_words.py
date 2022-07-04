import unittest

def reverse_letters(message, left_index, right_index ):
    
    while left_index < right_index:
        message[left_index], message[right_index] = message[right_index], message[left_index]
        left_index += 1
        right_index -= 1

def reverse_words(message):

    reverse_letters(message, 0, len(message) - 1)

    left_index = 0
    for index, ch in enumerate(message):
        if ch == " ":
            reverse_letters(message, left_index, index - 1)    
            left_index = index + 1
    if left_index < len(message) - 1:
        reverse_letters(message, left_index, len(message) - 1)    

    print("".join(message))
    return "".join(message)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        (['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l'], "steal pound cake"),
        ([''], ""),
        ([], "")
    ]

    def test_reverse_words(self):
        for test_array, expected in self.data:
            actual = reverse_words(test_array)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()


