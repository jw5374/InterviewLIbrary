def minStartValue(nums: list[int]) -> int:
    runningSum = 0
    minSum = 0
    for num in nums:
        runningSum += num
        if runningSum < minSum:
            minSum = runningSum
    return abs(minSum) + 1
