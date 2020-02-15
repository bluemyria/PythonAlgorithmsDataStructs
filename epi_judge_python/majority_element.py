from test_framework import generic_test

# 17.5 Find the majority element
# You are reading a sequence of strings. You know a priori thatmore than half 
# the strings are repetitions of a single string (the "majority element") but 
# the positions where the majority element occurs are unknown. Write a program
# that makes a single pass over the sequence and identifies the majority element.
#  For example, if the input is \b,a,c,A,a,b,a,a,c,a>, then a is the majority element
#  (it appears in 6 out of the 10 places)
def majority_search(stream):
    elem, count = None, 0
    for e in stream:
        if count == 0:
            elem = e
            count += 1
        elif elem == e:
            count += 1
        elif elem != e:
            count -= 1
        #print(e, elem, count)
    return elem


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
