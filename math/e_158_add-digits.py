# Problem link: https://leetcode.com/problems/add-digits/
# Repeatedly add digits until result is single digit
# Example: 1236 -> 1+2+3+6=12 -> 1+2=3


# O(log n) solution - iterative digit sum
def addDigits_basic(num: int) -> int:
    while num > 9:
        sum = 0
        while num:
            sum += num % 10
            num //= 10
        num = sum
    return num


# O(1) solution using digital root formula
def addDigits_efficient(num: int) -> int:
    if num == 0:
        return num
    return 1 + ((num - 1) % 9)


# Testing

result = addDigits_basic(1236)
print(result)
result = addDigits_efficient(1239)
print(result)
