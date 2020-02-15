import functools, itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

# 17.6 The Gasup Problem
# a number of cities are arranged on a circular road. You need to visit all the
# cities and come back to the starting city. A certain amount of gas is available
# at each city. The amount of gas summed up over all cities is equal to the amount
# of gas required to go around the road once. Your gas tank has unlimiled capacity.
# Call a city arnple if you can begin at that city with an empty tank, refill at it,
# then travel through all the remaining cities, refilling at each, and return
# to the ample city, without running out of gas at any point. 

# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    # SOS!!! don't forget to accumulate the fuel difference
    # find the lowest and start from the next city!
    fuel_after = list(itertools.accumulate(
        [ gallons[i]-distances[i]//MPG for i in range(len(gallons))]))
    return fuel_after.index(min(fuel_after))+1
    

@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
