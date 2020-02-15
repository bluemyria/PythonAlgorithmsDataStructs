import collections
import string
from test_framework import generic_test

# 18.7 Transform one string to another
# Uses BFS to find the least steps of transformation.
# Given a dictionary D and two strings s and t,write a program to determine
# if s produces f. Assume that all characters are lowercase alphabets. 
# If s does produce t, output the length of a shortest production sequence;
# otherwise, output -1.
def transform_string(D, s, t):

    StringWithDistance = collections.namedtuple(
        'StringWithDistance', ('candidate_string', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)  # Marks s as visited by erasing it in D.
    
    while q:
        curr = q.popleft()
        if curr.candidate_string == t:
            return curr.distance

        for i in range(len(curr.candidate_string)):
            for ch in string.ascii_lowercase:
                new_st = curr.candidate_string[:i] + ch + curr.candidate_string[i+1:]
                if new_st in D:
                    q.append(StringWithDistance(new_st, curr.distance + 1))
                    D.remove(new_st)

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
