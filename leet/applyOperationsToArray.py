def applyOperation(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    for i, val in enumerate(nums):
        if i < (len(nums) - 1) and nums[i+1] == val:
            nums[i] = val * 2
            nums[i+1] = 0
    numPointer = 0
    for num in nums:
        if num != 0:
            res[numPointer] = num
            numPointer += 1
    return res


print(applyOperation([0, 1]))

