import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# 6.4 Replace and remove
# Write a program which takes as input an array of characters, and removes each 'b' and replaces
# each'a'by two 'd's. Specifically, along with the array, you are provided an integer-valued size. Size
# denotes the number of entries of the array that the operation is to be applied to. You do not have
# to worry about preserving subsequent entries. For example, if the array is (a,b,a,c,_) and the size
# is 4, then you can retum (d,d,d,d,c). You can assume there is enough space in the array to hold the
# final result.

def replace_and_remove(size, s):
    # delete and insert in an array w/o copying:
    # first delete, than calculate how much extra room you need
    # and start shifting from the end 
    # DO NOT FORGET!!
    # s[index-1:index+1] = 'dd'
    # overwrites index-1 and index, NOT index+1 !!!! 
    nr_a = 0
    write_index = 0
    for i in range(size):
        if s[i] == 'a':
            nr_a += 1
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
    
    read_index = write_index - 1
    final_size = write_index + nr_a
    write_index = read_index + nr_a
    for i in range(read_index,-1,-1):
        if s[i]  == 'a':
            s[write_index-1:write_index+1] = ['d','d']
            write_index -= 2 
        else:
            s[write_index] = s[i]
            write_index -= 1 

    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    replace_and_remove(3, ['a','s','d', ''])
    
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
