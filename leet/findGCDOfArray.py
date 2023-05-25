def findGCD(nums: list[int]) -> int:
    [smallest, largest] = [1001, 0]
    for num in nums:
        smallest = min(num, smallest)
        largest = max(num, largest)
    return gcd(largest, smallest)


# a >= b
def gcd(a: int, b: int) -> int:
    [left, right] = [a, b]
    while right > 0:
        newRight = left % right
        left = right
        right = newRight
    return left
