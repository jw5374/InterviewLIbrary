def findTheArrayConcVal(nums: list[int]) -> int:
    [left, right] = [0, len(nums) - 1]
    res = 0
    while left <= right:
        if left == right:
            res += nums[left]
            break
        res += (nums[left] * (10 ** digitCount(nums[right]))) + nums[right]
        left += 1
        right -= 1
    return res


def digitCount(n: int) -> int:
    res = 0
    while n > 0:
        n //= 10
        res += 1
    return res
