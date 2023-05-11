def runningSum(nums: list[int]) -> list[int]:
    running = [nums[0]] * len(nums)
    for i in range(1, len(nums)):
        running[i] = running[i-1] + nums[i]
    return running
