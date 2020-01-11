import functools
import math
import heapq

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# 10.4 Compute the k closest Stars
# Consider a coordinate system for the Milky Way, in which Earth is at (0,0,0). Model stars as points,
# and assume distances are in light years. The Milky Way consists of approximately 10**12 stars, and
# their coordinates are stored in a file.
# How would you compute the k stars which are closest to Earth?

# SOS!!! incoming Stars are already of class Star (see deeper in test code:
#        stars = [Star(*a) for a in stars]
# SOS!!! in python there is only min_heap so you have to use for sorting -distance
# SOS!!! "star" calls the __repr__ function!!!!
class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars, k):
    min_heap = []
    
    for star in stars:
        heapq.heappush(min_heap, (-star.distance, star))
        if len(min_heap) > k :
            heapq.heappop(min_heap)
    # print([x for x in heapq.nsmallest(k, min_heap)])
    return [ x[1] for x in heapq.nsmallest(k, min_heap)]


def comp(expected_output, output):
    if len(output) != len(expected_output):
        return False
    return all(
        math.isclose(s.distance, d)
        for s, d in zip(sorted(output), expected_output))


@enable_executor_hook
def find_closest_k_stars_wrapper(executor, stars, k):
    stars = [Star(*a) for a in stars]
    return executor.run(
        functools.partial(find_closest_k_stars, iter(stars), k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("k_closest_stars.py",
                                       "k_closest_stars.tsv",
                                       find_closest_k_stars_wrapper, comp))
