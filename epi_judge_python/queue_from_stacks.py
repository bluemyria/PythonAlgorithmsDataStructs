from test_framework import generic_test

# 8.8 Implement a Queue using stacks
# How would you implement a queue given a library implementing stacks?
# Hint: lt is impossible to solve this problem with a single stack.
class Queue:
    # SOS !!! check if Stack is empty before popping
    def __init__(self):
        self._enq = []
        self._deq = []

    def enqueue(self, x):
        self._enq.append(x)
        return

    def dequeue(self):
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
        if self._deq:
            return self._deq.pop()
        else:
            return None


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
