import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

# 15.1 The Towers of Hanoi problem
def compute_tower_hanoi(num_rings):
    def help_compute_tower_hanoi(nr_rings_to_move, from_peg, to_peg,
                                 use_peg):
        if nr_rings_to_move > 0:
            help_compute_tower_hanoi(nr_rings_to_move - 1, from_peg, use_peg, 
                                     to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            help_compute_tower_hanoi(nr_rings_to_move - 1, use_peg, to_peg,
                                     from_peg)
    
    result = []
    pegs =[list(reversed(range(1,num_rings+1)))
           ] + [[] for _ in range(1, NUM_PEGS)]
    help_compute_tower_hanoi(num_rings, 0, 1, 2)

    return result


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
        1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure("Illegal move from {} to {}".format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("hanoi.py", 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
