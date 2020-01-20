# Project Euler
# Problem 3: Largest prime factor


def factor(n: int) -> list:
    if n <= 1:
        raise ValueError("invalid number")

    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    d = 3
    while n != 1:
        if n % d == 0:
            n //= d
            factors.append(d)
        else:
            d += 2
    return factors


largest_fac = factor(600_851_475_143)
print(largest_fac[-1])
