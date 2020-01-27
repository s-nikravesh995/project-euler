# Project Euler
# Problem 5: Smallest multiple

# This problem is actually the process of finding least common multiple (lcm)
# of 2, 3, ..., 20 or lcm(2, 3, ..., 20).


# gcd(a, b, c) = gcd(a, gcd(b, c))
def gcd(*args: int) -> int:
    """Greatest common divisor of two or more integers."""
    if len(args) == 2:
        a, b = args
        r = a % b
        while r:
            a, b = b, r
            r = a % b

        result = b
    else:
        a, *b = args
        result = gcd(a, gcd(*b))
    return result


# lcm(a, b, c) = lcm(a, lcm(b, c))
def lcm(*args: int) -> int:
    """Least common multiple of two or more integers."""

    if len(args) == 2:
        a, b = args
        result = abs(a * b) / gcd(a, b)
    else:
        a, *b = args
        result = lcm(a, lcm(*b))
    return int(result)


nums = [i for i in range(2, 21)]
result = lcm(*nums)
print(result)
