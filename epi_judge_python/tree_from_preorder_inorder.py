from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

# 9.12 Reconstruct a binary tree from traversal data
# Given an inorder traversal sequence and a preorder traversal sequence 
# of a binary tree write a program to reconstruct the tree. Assume each node has a unique key.
# Hint: Focus on the root
def binary_tree_from_preorder_inorder(preorder, inorder):
    # SOS!!! include the line 
    # from binary_tree_node import BinaryTreeNode
    # SOS!!! you need this dictionary: node_to_inorder_idx
    # to work better w/ the indices of the inorder
    # SOS!!! think of when the subtrees are so small that you have to return None
    # in the helper function
    # SOS!!! I used preorder, inorder "umgekehrt" as args of the helper function :|
    # SOS!!!!!!!!!!! calculating the indices!!!!
    node_to_inorder_idx = { data: i  for i, data in enumerate(inorder)}
    # print(node_to_inorder_idx)
    # print(preorder)

    def binary_tree_from_preorder_inorder_helper(st_preorder, end_preorder, st_inorder, end_inorder):
        # print(st_inorder, end_inorder, st_preorder, end_preorder)
        if end_inorder <= st_inorder  or end_preorder <= st_preorder :
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[st_preorder]]
        left_subtree_size = root_inorder_idx - st_inorder
        # print("------ ",preorder[st_preorder]," ------")
        return BinaryTreeNode(preorder[st_preorder],
            binary_tree_from_preorder_inorder_helper(st_preorder + 1, st_preorder + 1 + left_subtree_size,
                st_inorder, root_inorder_idx),
            binary_tree_from_preorder_inorder_helper(st_preorder + 1 + left_subtree_size, end_preorder,
                root_inorder_idx + 1, end_inorder))

    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
