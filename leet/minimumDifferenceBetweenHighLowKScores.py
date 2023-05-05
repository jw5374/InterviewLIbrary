def minimumDifference(nums: list[int], k: int) -> int:
    nums.sort()
    minDiff = 100000
    for i in range(len(nums - k + 1)):
        minDiff = min(minDiff, nums[i+k-1] - nums[i])
    return minDiff

