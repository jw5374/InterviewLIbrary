def buildArray(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    for i, num in enumerate(nums):
        res[i] = nums[num]
    return res
