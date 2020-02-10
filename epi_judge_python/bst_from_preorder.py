from bst_node import BstNode
# class BstNode:
#     def __init__(self, data=None, left=None, right=None):
#         self.data, self.left, self.right = data, left, right

from test_framework import generic_test

# 14.5 Reconstruct a BST from traversal data
def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None
    
    point = next((i for i, val in enumerate(preorder_sequence)
                  if val > preorder_sequence[0]),
                  len(preorder_sequence))

    return BstNode(preorder_sequence[0],
                   rebuild_bst_from_preorder(preorder_sequence[1:point]),
                   rebuild_bst_from_preorder(preorder_sequence[point:]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
