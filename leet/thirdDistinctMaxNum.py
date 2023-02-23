def thirdMax(nums: list[int]) -> int:
    nums = set(nums)
    nums = sorted(nums, reverse=True)
    return nums[0] if len(nums) < 3 else nums[2]


print(thirdMax([2,2,3]))

