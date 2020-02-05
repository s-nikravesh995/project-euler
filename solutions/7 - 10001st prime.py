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

###############################################################################

# Approach 2:
# Another alternative is to find a upper bound that can guarantee there are
# at least 10001 primes up to this limit.
# We can use the inverse of prime counting function to find this limit.


def pi_inverse(n):
    """Returns an upper bound for prime counting inverse function (pi function).
    """
    upperbnd = (n + 1) * (log(n + 1) + log(log(n + 1)))
    return ceil(upperbnd)


def primes(n) -> list:
    """Returns primes less than n using Eratosthenes sieve algorithm."""
    if n <= 1:
        raise ValueError("invalid number")

    isprime = [True] * (n - 1)
    primes_list = []
    i = 2
    while i ** 2 <= n:
        if isprime[i - 2]:
            j = i ** 2
            while j <= n:
                isprime[j - 2] = False
                j += i
        i += 1
    for num in range(2, n - 1):
        if isprime[num - 2]:
            primes_list.append(num)
    return primes_list


limit = pi_inverse(10001)
primes_list = primes(limit)
result = primes_list[10000]  # Note that 10001 element has the index of 10000.
print(result)
