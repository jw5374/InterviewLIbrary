def maximumCount(nums: list[int]) -> int:
    [left, right] = [0, len(nums) - 1]
    while left < len(nums) and nums[left] <= -1:
        left += 1
    while right >= 0 and nums[right] >= 1:
        right -= 1
    return max(left, len(nums) - right - 1)
