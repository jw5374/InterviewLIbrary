def pivotIndex(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0
    rightSums = [0] * len(nums)
    sum = 0
    for i in range(len(nums) - 2, -1, -1):
        rightSums[i] = sum
        sum += nums[i]
    sum = 0
    for i in range(0, len(nums)):
        if sum == rightSums[i]:
            return i
        sum += nums[i]
    return -1


print(pivotIndex([-1,-1,0,0,-1,-1]))

