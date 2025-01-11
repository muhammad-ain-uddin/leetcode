# Problem link: https://leetcode.com/problems/power-of-two/
# Check if a number n is a power of two.
# Return true if n is a power of two, otherwise return false.

# Example:
# Input: 1 → Output: true
# Input: 16 → Output: true
# Input: 3 → Output: false


# Constraints:
# 231 <= n <= 231 - 1


# O(1) solution - Iterative approach
def isPowerOfTwo_iterative(n):
    x = 1
    while x < n:
        x *= 2
    return x == n


# O(1) solution - Bit manipulation approach
def isPowerOfTwo_bit(n):
    return n > 0 and (n & (n - 1)) == 0


# O(1) solution - Large modulo approach
def isPowerOfTwo_largeMod(n):
    return n > 0 and ((1 << 30) % n) == 0


# Testing

print("Iterative solution:")
print(isPowerOfTwo_iterative(1))
print(isPowerOfTwo_iterative(16))
print(isPowerOfTwo_iterative(-3))

print("\nBit manipulation solution:")
print(isPowerOfTwo_bit(1))
print(isPowerOfTwo_bit(16))
print(isPowerOfTwo_bit(3))

print("\nLarge modulo solution:")
print(isPowerOfTwo_largeMod(1))
print(isPowerOfTwo_largeMod(-16))
print(isPowerOfTwo_largeMod(3))
