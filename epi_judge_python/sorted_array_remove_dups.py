import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# 5.5 Delete Duplicates from a Sorted Array
# Write a program which takes as input a sorted array and updates it
# so that all duplicates have been removed and the remaining elements have
# been shifted left to fill the emptied indices. Return the number 
# of valid elements.

# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    # Do not delete! Just overwrite w/ valid data!!
    # use running indices
    if not A:
        return 0
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
