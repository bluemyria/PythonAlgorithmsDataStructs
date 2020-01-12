import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# 12.4 Compute the LCA, optimizing for close ancestors
def lca(node0, node1):
    # SOS!!! Why use a set? How do I add to a set?
    # what happens if one node reaches the root way before the other?
    visited_nodes = set()
    while node0 or node1:
        if node0:
            if node0 in visited_nodes:
                return node0
            else:
                visited_nodes.add(node0)
            node0 = node0.parent

        if node1:
            if node1 in visited_nodes:
                return node1
            else:
                visited_nodes.add(node1)
            node1 = node1.parent
    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))
