def distinctDifferenceArray(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    for i in range(len(nums)):
        res[i] = len(set(nums[:i+1])) - len(set(nums[i+1:]))
    return res
