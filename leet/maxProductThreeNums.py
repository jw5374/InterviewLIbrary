def maximumProduct(nums: list[int]) -> int:
    if len(nums) == 3:
        return nums[0] * nums[1] * nums[2]
    nums.sort()
    return nums[-1] * nums[-2] * nums[-3] if nums[-1] * nums[-2] * nums[-3] > nums[0] * nums[1] * nums[-1] else nums[0] * nums[1] * nums[-1]


print(maximumProduct([1,2,3,4]))

