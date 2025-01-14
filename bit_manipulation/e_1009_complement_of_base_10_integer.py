# Problem link: https://leetcode.com/problems/complement-of-base-10-integer/

# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.

# Given an integer n, return its complement.

# Example:
# Input: 5  => Output: 2 (101 => 010)
# Input: 7  => Output: 0 (111 => 000)
# Input: 10 => Output: 5 (1010 => 0101)

# Constraints:
# 0 <= n < 10^9


# O(log n) solution - Iterative approach
def bitwiseComplement_iterative(n: int) -> int:
    # Handle the special case where n is 0
    if n == 0:
        return 1  # The complement of 0 is 1

    result = 0
    position_value = 1  # Represents the current bit position (1, 2, 4, 8, ...)

    # Process each bit of the number from right to left
    while n:
        current_bit = n % 2  # Get the least significant bit (LSB)
        flipped_bit = (
            current_bit ^ 1
        )  # Flip the bit using XOR: 0 becomes 1, 1 becomes 0
        n //= 2  # Remove the processed bit by right shifting

        # Build the result by adding the flipped bit at the current position
        result += flipped_bit * position_value
        position_value *= 2  # Move to the next bit position

    return result


# O(log n) solution - Bitmask approach
def bitwiseComplement_bitmask(n: int) -> int:
    # Handle the special case where n is 0
    if n == 0:
        return 1  # The complement of 0 is 1

    temp = n
    bitmask = 0

    # Create a bitmask with the same number of bits as input
    # For example, if n = 5 (101), mask becomes 111
    while temp:
        bitmask = (bitmask << 1) | 1  # Add 1 to the right of current mask
        temp >>= 1  # Right shift to process next bit

    # Use bitwise NOT (~) on n and AND (&) with mask to get complement
    # The mask ensures we only get relevant bits
    return (~n) & bitmask


# Testing

print("Iterative approach:")
print(bitwiseComplement_iterative(5))
print(bitwiseComplement_iterative(16))
print(bitwiseComplement_iterative(7))

print("Bitwise approach:")
print(bitwiseComplement_bitmask(0))
print(bitwiseComplement_bitmask(1))
print(bitwiseComplement_bitmask(1024))
