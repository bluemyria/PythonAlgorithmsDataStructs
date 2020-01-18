# P1:   Multiples of 3 and 5
# Find the sum of all the multiples of 3 or 5 below 1000.
result = sum(x for x in range(1000) if x%3 == 0 or x%5 == 0)
print(result)

# P2:   Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def fib_sum(limit):
    f1, f2, sum = 1, 2, 0
    while f2 < limit:
        if f2%2 == 0:
            sum = sum + f2
        f1, f2 = f2, f1+f2
    return sum
print(fib_sum(4000000))