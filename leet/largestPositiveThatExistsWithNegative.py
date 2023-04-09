def findMaxK(nums: list[int]) -> int:
    negatives = {}
    positives = {}
    maxNum = -1
    for num in nums:
        if num < 0:
            negatives[num] = True
        else:
            positives[num] = True
    for num in positives.keys():
        if (num * -1) in negatives:
            maxNum = max(maxNum, num)
    return maxNum
