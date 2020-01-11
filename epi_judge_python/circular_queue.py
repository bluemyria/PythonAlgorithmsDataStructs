from test_framework import generic_test
from test_framework.test_failure import TestFailure

# 8.7 Implement a Circular Queue
# Implement a queue API using an array for storing elements. Your API should include a constructor
# function which takes as argument the initial capacity of the queue, enqueue and dequeue functions,
# and a function which returns the number of elements stored. Implement dynamic resizing to
# support storing an arbitrarily large number of elements.
# Hint:Track the head and tail. How can you differentiate a full queue from an empty one?
class Queue:
    # SOS!!! Usage of scale Factor, I placed the -1 in the wrong place
    # SOS!!! check what makes the elements to appear consecutively 
    # self._entries = self._entries[self._head:] + self._entries[:self._head]
    # SOS!!! self._tail shows the next empty position and always exists!!
    # because resizing happens before enqueueing!!!
    # SOS!!! moving the head and the tail (+1) only w/ % len(array) in case they have
    # to be "rewinded"        
    SCALE_FACTOR = 2
    
    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = 0
        self._used_size = 0

    def enqueue(self, x):
        # print("enqueue\n")
        #  resize
        if self._used_size == len(self._entries):
            # print("resize\n")
            self._entries = self._entries[self._head:] + self._entries[:self._head]
            self._head = 0
            self._tail = self._used_size
            self._entries += [None] * (Queue.SCALE_FACTOR -1) * len(self._entries)
        
        self._entries[self._tail] = x
        self._used_size += 1
        self._tail = (self._tail + 1) % len(self._entries)
        # print("\n-----------", self._entries)
        # print(x, self._head, self._tail, self._used_size)

    def dequeue(self):
        # print("dequeue\n")
        x = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        self._used_size -= 1
        # print("\n-----------", self._entries)
        # print(self._head, self._tail, self._used_size)
        return x

    def size(self):
        # print("size\n")
        # print("\n-----------", self._entries)
        # print(self._head, self._tail, self._used_size)

        return self._used_size


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
