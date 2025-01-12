# Problem link: https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is a palindrome , and false otherwise.

# An integer is a palindrome when it reads the same forward and backward.
# For example, 121 is a palindrome while 123 is not.

# Example:
# Input: 121  → Output: True
# Input: -121 → Output: False
# Input: 10   → Output: False

# Constraints:
# -231 <= x <= 231 - 1


# O(log n) solution - Reverse number approach
def isPalindrome(x):
    if x < 0:
        return False

    num = x
    reverse = 0

    while num:
        last_digit = num % 10
        num = num // 10
        reverse = (reverse * 10) + last_digit

    return x == reverse


# Testing

print("Reverse number approach:")
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
