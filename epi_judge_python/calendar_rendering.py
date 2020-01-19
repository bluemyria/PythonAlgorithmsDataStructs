import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# 13.5 Render a calendar
# Write a program that takes a set of events, and determines the maximum number 
# of events that take place concurrently.
# Example input: [[0, 2], [0, 7], [1, 6], [5, 6]]
def find_max_simultaneous_events(A):
    # SOS!!! sort by event time, start, stop mixed!!!
    sim_events, max_sim_events = 0, 0
    events = [(x[0], True) for x in A ] + [(x[1], False) for x in A ] 
    events.sort(key = lambda x: x[0])
    for e in events:
        if e[1]:
            sim_events += 1
            max_sim_events = max(sim_events, max_sim_events)
        else:
            sim_events -= 1
    return max_sim_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
