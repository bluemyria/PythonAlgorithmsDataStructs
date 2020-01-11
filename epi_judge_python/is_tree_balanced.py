from test_framework import generic_test
import collections

# 9.1 Test is a binary tree is height balanced
# A  binary tree is said to be height-balanced if for each node in the tree, 
# the difference in the height of its left and right subtrees is at most one. 
# A perfect binary tree is height-balanced, as is a complete binary tree. 
#  A height-balanced binary tree does not have to be perfect or complete
def is_balanced_binary_tree(tree):
    # SOS!!! the definition of named tuples!
    # SOS!!! definition of helper_function for recursive calls
    # SOS!!! max usage requires commas!!!
    # SOS!!! return immediatelly if one subtree unbalanced!
    # SOS!!! depth_under_it max of the two subtrees + 1! 
    
    BalancedStWithHeight = collections.namedtuple('BalancedStWithHeight', ("depth_under_it","balanced"))
    
    def helper_balanced_binary_tree(tree):
        if not tree: 
            return BalancedStWithHeight(0, True)
        # print(tree)

        bbtl = helper_balanced_binary_tree(tree.left)
        if not bbtl.balanced:
            return BalancedStWithHeight(0, False)
        
        bbtr = helper_balanced_binary_tree(tree.right)
        if not bbtr.balanced:
            return BalancedStWithHeight(0, False)
        
        balanced = abs(bbtl.depth_under_it - bbtr.depth_under_it) <= 1
        depth_under_it = max(bbtl.depth_under_it, bbtr.depth_under_it) + 1
        # print(tree.data, depth_under_it, balanced)
        return BalancedStWithHeight(depth_under_it, balanced)
    
    return helper_balanced_binary_tree(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
