# Problem link: https://leetcode.com/problems/add-digits/
# Repeatedly add digits until result is single digit
# Example: 1236 -> 1+2+3+6=12 -> 1+2=3

def addDigits_basic(num: int) -> int:
    # O(log n) solution - iterative digit sum
    while num > 9:
        sum = 0
        while num:
            sum += num % 10
            num //= 10
        num = sum
    return num

def addDigits_efficient(num: int) -> int:
    # O(1) solution using digital root formula
    if num == 0:
        return 0
    return 1 + ((num - 1) % 9)

result = addDigits_basic(1236)
print(result)
result = addDigits_efficient(1239)
print(result)