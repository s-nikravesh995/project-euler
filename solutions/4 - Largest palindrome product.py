# Project Euler
# Problem 4: Largest palindrome product


def is_plaindrome(num: int) -> bool:
    num = str(num)
    if num[::-1] == num:
        return True
    return False


# Performance notes:
#   1: We can assume that b >= a. Because, for example, the number 69696 is
#      both checked when a = 132 and b = 528 and when a = 528 and b = 132.
#
#   2: Let's assume that P = 100000x + 10000y + 1000z + 100z + 10y + x
#      P = 100001x + 10010y + 1100z = 11(9091x + 10010y + 1100z).
#      This means either a or b is a multiple of 11. Using this information
#      we can avoid checking all of the numbers.
#      When a is not a multiple of 11, b has to be and, vice versa.


largest_pdrome = 0
a = 999
b = 990

while a >= 100:
    if a%11 == 0:
        b = 999
        diff = 1
    else:
        b = 990
        diff = 11

    while b >= a:
        num = a * b
        if is_plaindrome(num):
            if num > largest_pdrome:
                largest_pdrome = num
        b -= diff
    a -= 1

print(largest_pdrome)
