from test_framework import generic_test

# 14.2 Find the first key greater than a given value in a BST
# Write a program that takes as input a BST and a value, and retums the first key that would appear
# in an inorder traversal which is greater than the input value.
# Hint: Pertorm binary search, keeping some additional state.
def find_first_greater_than_k(tree, k):
    
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far = subtree
            subtree = subtree.left
        else:
            subtree = subtree.right
    return first_so_far


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
