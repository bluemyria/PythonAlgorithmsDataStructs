from test_framework import generic_test
import math

# 5.9 Enumerate all primes up to n
# Given n, return all primes up to and including n.
# For example, if the input is 18, you should return <2,3,5,7,11,13,17>.
def generate_primes(n):
    # SOS!! initialise Array w/ True, False!!!!
    # SOS!!! return a part of the results, based on a condition
    # SOS!!! check if a number is prime
    if n < 2:
        return []
    raw_primes = [False] * 2 + [True] * (n - 1)
    for i in range(2, n+2):
        if is_prime(i):
            for j in range(2, n//i+1):
                raw_primes[j*i] = False 
        else:
            for j in range(1, n//i+1):
                raw_primes[j*i] = False 
    return [i for i in range(len(raw_primes)) if raw_primes[i] == True ]

def is_prime(m):
    return all(m%i != 0 for i in range(2, int(math.sqrt(m)) ) )


def old_is_prime(m):
    for i in range(2, int(math.sqrt(m))):
        if m%i == 0:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("prime_sieve.py", "prime_sieve.tsv",
                                       generate_primes))
