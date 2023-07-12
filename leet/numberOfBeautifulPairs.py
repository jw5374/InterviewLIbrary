import math


def countBeautifulPairs(nums: list[int]) -> int:
    res = 0
    for i in range(len(nums)-1):
        j = i + 1
        first = nums[i] // (10 ** math.floor(math.log(nums[i], 10)))
        while j < len(nums):
            second = nums[j] % 10
            [left, right] = [max(first, second), min(first, second)]
            if gcd(left, right) == 1:
                res += 1
            j += 1
    return res


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)
