# Project Euler
# Problem 2: Even Fibonacci numbers


a, b = 1, 2
fib_sum = 0
while a < 4_000_000:
    a, b = b, a+b
    if a%2 == 0:
        fib_sum += a
print(fib_sum)
