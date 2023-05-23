def findClosestNumber(nums: list[int]) -> int:
    minNum = 100000
    retVal = 0
    for num in nums:
        minNum = min(abs(num), minNum)
        if (num * -1 == minNum and retVal != num * -1) or (num == minNum and retVal != num):
            retVal = num
    return retVal
