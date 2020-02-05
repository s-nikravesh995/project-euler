# Project Euler
# Problem 6: Sum square difference


# 1 + 2 + ... + n = (n * (n + 1)) / 2
# (1 + 2 + ... + n) ^ 2 = 1^3 + 2^3 + ... + n^3 = (n^2 * (n + 1)^2) / 4
# 1^2 + 2^3 + ... + n^2 = (n * (n + 1) * (2*n + 1)) / 6

n = 100
result = (n**2 * (n + 1)**2) / 4 \
         - (n * (n + 1) * (2*n + 1)) / 6
result = int(result)
print(result)
