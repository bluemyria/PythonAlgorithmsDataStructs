from test_framework import generic_test

# 8.6 Compute Binary Tree Nodes in Order of increasing depth
# Given a binary tree, return an array consisting of the keys at the same level. Keys should appear
# in the order of the corresponding nodes' depths, breaking ties from left to right. 
# Hint: First think about solving this problem with a pair of queues
# (A pair of arrays I would rather say).
def binary_tree_depth_order(tree):
    # This expression mixed e up
    # print( [child for curr in curr_depth_nodes for child in (curr.left, curr.right) if child])
        
    result = []
    if not tree:
        return result
    
    # print("TREE:-----------------------", tree)
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child for curr in curr_depth_nodes for child in (curr.left, curr.right) if child
        ]
        # print(result)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
