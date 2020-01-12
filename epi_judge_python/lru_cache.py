from test_framework import generic_test
from test_framework.test_failure import TestFailure
import collections

# 12.3 Implement an ISBN cache
# Create a cache for looking up prices of books identified by their ISBN. You implement lookup,
# insert, and remove methods. Use the Least Recently Used (LRU) policy for cache eviction. If an
# ISBN is already present, insert should not change the price, but it should update that entry tobe the
# most recently used entry. Lookup should also update that entry to be the most recently used entry.
class LruCache:
    # SOS!!! An OrderedDict is a dictionary subclass that remembers 
    # the order that keys were first inserted.
    # .popitem() is LIFO unless you give the param last=True, then it pops FIFO!!!
    def __init__(self, capacity):
        self._isbns = collections.OrderedDict()
        self._capacity = capacity
        
    def lookup(self, isbn):
        if isbn not in self._isbns:
            return -1
        else:
            price = self._isbns.pop(isbn)
            self._isbns[isbn] = price
        return price

    def insert(self, isbn, price):
        if isbn in self._isbns:
            price = self._isbns.pop(isbn) 
        elif len(self._isbns) == self._capacity:
            self._isbns.popitem(last=False)
        self._isbns[isbn] = price

    def erase(self, isbn):
        return self._isbns.pop(isbn, None) is not None


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
