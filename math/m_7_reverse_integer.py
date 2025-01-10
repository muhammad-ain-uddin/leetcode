# Problem link: https://leetcode.com/problems/reverse-integer/
# Reverse a 32-bit signed integer.
# Return 0 if the result overflows.

# Example:
# Input: 123 → Output: 321
# Input: -123 → Output: -321
# Input: 120 → Output: 21

# Constraints:
# -2^31 <= x <= 2^31 - 1

import math


# O(log |x|) solution - iteration
def reverse(x):
    MIN = -2147483648  # -2^31,
    MAX = 2147483647  #  2^31 - 1

    res = 0
    while x:
        digit = int(math.fmod(x, 10))  # (python dumb) -1 % 10 = 9
        x = int(x / 10)  # (python dumb) -1 // 10 = -1

        if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
            return 0
        if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
            return 0

        res = (res * 10) + digit

    return res


print(reverse(123))
print(reverse(-123))
print(reverse(120))
