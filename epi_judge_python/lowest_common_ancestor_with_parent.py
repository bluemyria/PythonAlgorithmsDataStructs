import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import collections

# 9.4 Compute the LCA when Nodes have parent pointers
def lca(node0, node1):
    # SOS!!! for a binary tree w/ just one node (1), it was
    # expected to return the 1 (root)!!
    # Clarify what is expected !! find examples and ask!! 
    Genealogy = collections.namedtuple('Genealogy', ('depth', 'anc'))
    def analyse_depth(node):
        depth = 1
        anc = []
        anc.append(node)
        while node.parent:
            depth += 1
            anc.append(node.parent) 
            node = node.parent
        return Genealogy(depth, anc)
    
    gen0 = analyse_depth(node0)
    gen1 = analyse_depth(node1)
    
    diff_depth =  gen0.depth - gen1.depth
    
    # The following did not work as 
    # anc_short, anc_long = gen0.anc, gen1.anc if...... else gen1.anc, gen0.anc
    # was throwing error "too many values to unpack"!!!
    if diff_depth < 0:
        anc_short, anc_long = gen0.anc, gen1.anc
    else:
        anc_short, anc_long = gen1.anc, gen0.anc
    for i in range(abs(diff_depth),len(anc_long)):
        if anc_long[i] in anc_short:
            return anc_long[i]
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
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
