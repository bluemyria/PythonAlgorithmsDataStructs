from test_framework import generic_test

# 9.11 Implement an Inorder traversal with O(1) Space
# Write a nonrecursive program for computing the inorder traversal sequence for a binary tree.
# Assume nodes have parent fields.
# Hint: How can you tell whether a node is a left child or right child of its parent?
def inorder_traversal(tree):
    # the code is much better w/ curr than w/ tree!!!!!!
    prev, result = None, []
    curr = tree
    while curr:
        if prev == curr.parent:
            if curr.left:
                next = curr.left
                prev = curr    
            else:
                result.append(curr.data)
                next = curr.right or curr.parent
                prev = curr
        elif prev == curr.left:
            result.append(curr.data)
            next = curr.right or curr.parent
            prev = curr        
        else:
            next = curr.parent
        prev = curr
        curr = next

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
