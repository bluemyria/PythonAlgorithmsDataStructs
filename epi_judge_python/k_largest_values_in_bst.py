from test_framework import generic_test, test_utils


# 14.3. Find the k largest elements in a BST
# Write a program that takes as input a BST and an integer k, and retums the k largest elements in the
# BST in decreasing order. 
def find_k_largest_in_bst(tree, k):
    
    def find_k_largest_in_bst_helper(tree):
        if tree and len(k_largest) < k:
            find_k_largest_in_bst_helper(tree.right)
            # SOS!!! checkagain if k is reached!!!
            if len(k_largest) < k:
                k_largest.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)
        return

    k_largest = []
    find_k_largest_in_bst_helper(tree)
    return k_largest

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
