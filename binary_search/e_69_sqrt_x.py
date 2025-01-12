# Problem link: https://leetcode.com/problems/sqrtx/
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part is returned.

# Example:
# Input: 4 → Output: 2
# Input: 8 → Output: 2 (Square root of 8 is 2.82842..., truncated to 2)

# Constraints:
# 0 <= x <= 231 - 1


# O(log n) solution - Binary search approach
def mySqrt(x):
    start, end = 0, x
    result = 0

    while start <= end:
        mid = start + ((end - start) // 2)

        if mid**2 > x:
            end = mid - 1
        elif mid**2 < x:
            start = mid + 1
            result = mid
        else:
            return mid
    return result


# Testing

print("Binary search solution:")
print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(31))
