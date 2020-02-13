import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

# 16.6 The knapsack problem
def optimum_subject_to_capacity(items, capacity):

    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            return 0

        if V[k][available_capacity] == -1:
            without_last_item = optimum_subject_to_item_and_capacity(
                k-1, available_capacity)
            
            with_last_item = (0 if items[k].weight > available_capacity
                else items[k].value + optimum_subject_to_item_and_capacity(
                   k-1, available_capacity - items[k].weight))
            
            V[k][available_capacity] = max(
                without_last_item, with_last_item)
        return V[k][available_capacity]
    
    V = [[-1] * (capacity + 1) for _ in items ]
    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
