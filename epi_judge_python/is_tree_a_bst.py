from test_framework import generic_test

# 14.1 Test if a binary tree satisfies the BST property
# Write a Program that takes as input a binary tree and checks if the tree satisfies the BST property
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    # sos!! no 2 same values in the tree
    if not tree:
        return True
    elif low_range > tree.data or tree.data > high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and 
            is_binary_tree_bst(tree.right, tree.data, high_range) )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
