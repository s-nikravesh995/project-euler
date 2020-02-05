# Project Euler
# Problem 7: 10001st prime


from array import array
from math import log, ceil


# Approach 1:
# In this approach we use a prime number generator. We keep producing
# primes until we reach the 10001st one.


# The function produces 2 and 3 as prime numbers. "primes" keeps track of
# found primes. The "prime_gen" checks if "num" is divisible by found primes
# or not. If it is not divisible by found primes, it spits out "num" and
# appends "num" to "primes".

def prime_gen():
    """A generator to produce prime numbers."""
    def isprime(n):
        for i in primes:
            if n % i == 0:
                return False
            if i ** 2 > n:
                return True

    primes = array('I', [3])
    num = 3

    yield 2
    yield 3

    while True:
        num += 2
        if isprime(num):
            primes.append(num)
            yield num


count = 0
for i in prime_gen():
    count += 1
    if count == 10001:
        result = i
        break

print(result)
