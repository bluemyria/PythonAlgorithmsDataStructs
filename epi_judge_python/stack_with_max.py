from test_framework import generic_test
from test_framework.test_failure import TestFailure

# 8.1 Implement a Stack with max API
# Design a stack that includes a max operation, in addition to push and pop. The max method should
# return the maximum value stored in the stack.
# Hint: Use additional storage to track the maximum value
class Stack:
    # Take care of Index out of Bound errors
    # check them in every method!!
    #  or raise IndexError
    def __init__(self):
        self.st = []
        self.max_st = []

    def empty(self):
        return self.st == []

    def max(self):
        if self.empty():
            return 0 
        else:
            return self.max_st[-1]

    def pop(self):
        if self.empty():
            return []
        if self.max_st[-1] == self.st[-1]:
            self.max_st.pop()
        return self.st.pop()

    def peek(self):
        if self.empty():
            return []
        return self.st[-1]

    def push(self, x):
        # what does push return?
        self.st.append(x)
        if self.max_st == [] or self.max_st[-1] < x:
            self.max_st.append(x)
        return x


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                print("Pop: expected " + str(arg) + ", got " + str(result))
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                print("Max: expected " + str(arg) + ", got " + str(result))
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                print("Empty: expected " + str(arg) + ", got " + str(result))
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
