from test_framework import generic_test
import string

# 8.2 Evaluate RPN expressions
# Write a program that takes an arithmetical expression in RPN
# and returns the number that the expression evaluates to.
#  example "3,4,+,2,*,45-"
def evaluate(expression):
    # SOS!!! split input string!! not single chars as input!!
    # SOS!!! check how to make a dict w/ lambdas!!!
    # SOS!!! check what the expression returns, not if it is valid (in this case)
    evst = []
    expr_arr = expression.split(",")
    # print(evst)
    # print("expr_arr",expr_arr)
    ops = {'+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x // y}
    for val in expr_arr:
        if val not in ops.keys():
            evst.append(int(val))
        else:
            evst.append(ops[val](evst.pop(),evst.pop()))
        # print(evst)
    return evst[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
