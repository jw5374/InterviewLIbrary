def specialArray(nums: list[int]) -> int:
    nums.sort()
    for i, num in enumerate(nums):
        if len(nums) - i <= num and (len(nums) - i > nums[i-1] or i == 0):
            return len(nums) - i
    return -1
