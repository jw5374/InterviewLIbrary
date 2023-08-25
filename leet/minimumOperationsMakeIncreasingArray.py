def minOperations(nums: list[int]) -> int:
    prevNum = nums[0]
    res = 0
    for i in range(1, len(nums)):
        if prevNum >= nums[i]:
            res += (prevNum + 1) - nums[i]
            prevNum += 1
        else:
            prevNum = nums[i]
    return res
