def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxRepeat = 0
    i = 0
    while i < len(nums):
        if nums[i] == 1:
            currInd = i
            while i < len(nums) and nums[i] == 1:
                i += 1
            maxRepeat = max(maxRepeat, i - currInd)
        i += 1
    return maxRepeat


print(findMaxConsecutiveOnes([1,0,1,1,0,1]))

