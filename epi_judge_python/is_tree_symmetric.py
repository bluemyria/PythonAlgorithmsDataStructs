from test_framework import generic_test

# 9.2 Test if a binary tree is symmetric
# A binary tree is symmetric if you can draw a vertical line through 
# the root and then the left subtree is the mirror image of the right subtree. 
def is_symmetric(tree):
    # SOS!!! return not tree
    # returns true if empty and protects IndexErrors from the next call to check_symmetric
    def check_symmetric(tree_left, tree_right):
        if not tree_left and not tree_right:
            return True
        elif tree_left and tree_right:
            return (tree_left.data == tree_right.data
                and check_symmetric(tree_left.right, tree_right.left)
                and check_symmetric(tree_left.left, tree_right.right))
        else:
            return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
