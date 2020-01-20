# Project Euler
# Problem 1: Multiples of 3 and 5


multiples = (i for i in range(1000) if (i%3 == 0 or i%5 == 0))
result = sum(multiples)
print(result)
