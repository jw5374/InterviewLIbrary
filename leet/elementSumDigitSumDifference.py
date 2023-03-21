def differenceOfSum(nums: list[int]) -> int:
    digits = 0
    elements = 0
    for num in nums:
        digits += digitSum(num)
        elements += num
    return digits - elements if digits > elements else elements - digits


def digitSum(n: int) -> int:
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


print(differenceOfSum([1,15,6,3]))

